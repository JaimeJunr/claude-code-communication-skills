#!/usr/bin/env python3
"""Sync the communication stack from its upstream repositories.

Reads stack.json, fetches every upstream at its ref, copies the selected
paths into plugins/<plugin>, applies compatibility patches and regenerates
the marketplace manifest, THIRD_PARTY_NOTICES.md, UPSTREAM.lock and the
skill tables in README.md and README.pt-BR.md. Reference-only sources copy
into a hand-written plugin without replacing its owned files or manifest.

    python3 scripts/sync.py                 # fetch upstreams and rebuild
    python3 scripts/sync.py --src ./cache   # reuse clones named <owner>_<repo>
    python3 scripts/sync.py --check         # validate the tree, change nothing

Standard library only, so it runs anywhere Python 3.9+ does.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
STACK = json.loads((ROOT / "stack.json").read_text())
LOCK_PATH = ROOT / "UPSTREAM.lock"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
KEYWORDS = ["communication", "writing", "clarity", "output-styles", "claude-code", "skills"]


def run(*cmd: str, cwd: Path | None = None) -> str:
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def fetch(repo: str, ref: str, src_dir: Path | None, cache: dict[str, Path], tmp: Path) -> Path:
    if repo in cache:
        return cache[repo]
    local = src_dir / repo.replace("/", "_") if src_dir else None
    if local and not local.is_dir():
        sys.exit(f"source: {local} not found; --src never fetches missing clones")
    if local and local.is_dir():
        path = local
    else:
        path = tmp / repo.replace("/", "_")
        run("git", "clone", "--quiet", "--depth", "1", "--branch", ref,
            f"https://github.com/{repo}.git", str(path))
    cache[repo] = path
    return path


def frontmatter(text: str) -> dict[str, str]:
    """Top-level scalar keys of a SKILL.md frontmatter (enough for name/description)."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return out


def patch_description(skill_md: Path, description: str) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    if not m:
        sys.exit(f"patch: {skill_md} has no frontmatter")
    lines = m.group(1).splitlines()
    idx = next((i for i, l in enumerate(lines) if l.startswith("description:")), None)
    if idx is None:
        sys.exit(f"patch: {skill_md} has no description")
    end = idx + 1
    if re.fullmatch(r"description:\s*[>|][+-]?\s*", lines[idx]):
        # O bloco termina na próxima chave; metadados vizinhos precisam sobreviver.
        while end < len(lines) and (not lines[end].strip() or lines[end][0].isspace()):
            end += 1
    elif end < len(lines) and lines[end].strip() and lines[end][0].isspace():
        sys.exit(f"patch: {skill_md} description has unsupported continuation, review the patch")
    escaped = description.replace("\\", "\\\\").replace('"', '\\"')
    lines[idx:end] = [f'description: "{escaped}"']
    skill_md.write_text("---\n" + "\n".join(lines) + "\n---\n" + text[m.end():])


def drop_frontmatter_keys(skill_md: Path, keys: list[str]) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    if not m:
        sys.exit(f"patch: {skill_md} has no frontmatter")
    lines = m.group(1).splitlines()
    for key in keys:
        kept = [l for l in lines if not l.startswith(f"{key}:")]
        if len(kept) == len(lines):
            sys.exit(f"patch: {skill_md} has no frontmatter key {key!r}, review the patch")
        lines = kept
    skill_md.write_text("---\n" + "\n".join(lines) + "\n---\n" + text[m.end():])


def set_frontmatter_keys(skill_md: Path, values: dict) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    if not m:
        sys.exit(f"patch: {skill_md} has no frontmatter")
    lines = m.group(1).splitlines()
    for key, value in values.items():
        line = f"{key}: {json.dumps(value, ensure_ascii=False)}"
        idx = next((i for i, item in enumerate(lines) if item.startswith(f"{key}:")), None)
        if idx is None:
            lines.append(line)
        else:
            lines[idx] = line
    skill_md.write_text("---\n" + "\n".join(lines) + "\n---\n" + text[m.end():])


def replace_in_body(skill_md: Path, pattern: str, replacement: str,
                    expected_count: int | None = None) -> None:
    text = skill_md.read_text()
    m = FRONTMATTER.match(text)
    head, body = (text[:m.end()], text[m.end():]) if m else ("", text)
    new_body, count = re.subn(pattern, replacement, body)
    # Um patch sem correspondência voltaria a distribuir a regra incompatível.
    if count == 0:
        sys.exit(f"patch: {skill_md} has no match for {pattern!r}, review the patch")
    if expected_count is not None and count != expected_count:
        sys.exit(f"patch: {skill_md} matched {count}, expected {expected_count} for {pattern!r}, review the patch")
    skill_md.write_text(head + new_body)


def apply_patch(skill_md: Path, patch: dict) -> None:
    if "description" in patch:
        patch_description(skill_md, patch["description"])
    if "drop_keys" in patch:
        drop_frontmatter_keys(skill_md, patch["drop_keys"])
    if "frontmatter" in patch:
        set_frontmatter_keys(skill_md, patch["frontmatter"])
    if patch.get("model_invocable") is True:
        # Upstreams can restrict invocation; selected recipes must remain callable.
        key = "disable-model-invocation"
        if key in frontmatter(skill_md.read_text()):
            drop_frontmatter_keys(skill_md, [key])
    for rule in patch.get("replace", []):
        replace_in_body(skill_md, rule["pattern"], rule["with"], rule.get("count"))


def copy_path(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules", ".DS_Store"))
    else:
        shutil.copy2(src, dst)


def plugin_manifest(name: str, description: str, author: str, license_: str,
                    homepage: str, skills_path: str | None) -> dict:
    manifest = {
        "name": name,
        "description": description,
        "author": {"name": author},
        "homepage": homepage,
        "repository": STACK["marketplace"]["repository"],
        "license": license_,
        "keywords": KEYWORDS,
    }
    if skills_path:
        manifest["skills"] = skills_path
    return manifest


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def sync(src_dir: Path | None) -> None:
    old_lock = json.loads(LOCK_PATH.read_text()) if LOCK_PATH.exists() else {}
    lock: dict[str, dict] = {}
    cache: dict[str, Path] = {}
    shared: dict[str, Path] = {}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with tempfile.TemporaryDirectory() as tmp:
        for src in STACK["sources"]:
            upstream = fetch(src["repo"], src["ref"], src_dir, cache, Path(tmp))
            commit = run("git", "rev-parse", "HEAD", cwd=upstream)
            dest = PLUGINS / src["plugin"]
            reference_only = src.get("reference_only", False)
            if src["plugin"] in {p["plugin"] for p in STACK["local_plugins"]} and not reference_only:
                sys.exit(f"{src['id']}: copying into a local plugin requires reference_only")
            staging = Path(tmp) / "staging" / src["id"]
            staging.mkdir(parents=True)
            hashes: dict[str, str] = {}
            for item in src["copy"]:
                relative = Path(item["to"])
                if relative.is_absolute() or ".." in relative.parts:
                    sys.exit(f"{src['id']}: copy destination must be a contained relative path")
                origin = upstream / item["from"]
                if not origin.exists():
                    sys.exit(f"{src['id']}: {item['from']} not found upstream at {commit[:7]}")
                if reference_only and not Path(item["to"]).is_relative_to(src["license_dir"]):
                    sys.exit(f"{src['id']}: reference copy must stay inside {src['license_dir']}")
                target_plugin = item.get("plugin", src["plugin"])
                copy_staging = staging
                if target_plugin != src["plugin"]:
                    reference_root = Path("skills") / target_plugin / "references" / "upstream" / src["id"]
                    if target_plugin not in {p["plugin"] for p in STACK["local_plugins"]} or not Path(item["to"]).is_relative_to(reference_root):
                        sys.exit(f"{src['id']}: cross-plugin copy must stay inside an owned plugin's {reference_root}")
                    copy_staging = Path(tmp) / "shared" / target_plugin
                    shared[target_plugin] = copy_staging
                copy_path(origin, copy_staging / item["to"])
                files = sorted(origin.rglob("*")) if origin.is_dir() else [origin]
                for path in files:
                    if path.is_file():
                        hashes[path.relative_to(upstream).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
            for lic in src.get("license_files", []):
                origin = upstream / lic
                if not origin.is_file():
                    sys.exit(f"{src['id']}: license file {lic} not found upstream at {commit[:7]}")
                target = staging / src.get("license_dir", "") / Path(lic).name
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    shutil.copy2(origin, target)
                hashes[lic] = hashlib.sha256(origin.read_bytes()).hexdigest()
                previous_hash = old_lock.get(src["id"], {}).get("files", {}).get(lic)
                if previous_hash and previous_hash != hashes[lic]:
                    print(f"review: {src['id']} license/notice {lic} changed upstream")
            for p in src.get("patches", []):
                apply_patch(staging / p["file"], p)
            homepage = src.get("homepage", f"https://github.com/{src['repo']}")
            if not reference_only:
                write_json(staging / ".claude-plugin" / "plugin.json", plugin_manifest(
                    src["plugin"], src["description"], src["author"], src["license"],
                    homepage, src.get("skills_path")))
                if dest.exists():
                    shutil.rmtree(dest)
            shutil.copytree(staging, dest, dirs_exist_ok=True)
            prev = old_lock.get(src["id"], {})
            lock[src["id"]] = {
                "repo": src["repo"],
                "ref": src["ref"],
                "commit": commit,
                "license": src["license"],
                "files": hashes,
                "synced_at": prev.get("synced_at", now) if prev.get("commit") == commit else now,
            }
            print(f"  {src['id']:15} {src['repo']:40} {commit[:7]}")

        for plugin, staging in shared.items():
            shutil.copytree(staging, PLUGINS / plugin, dirs_exist_ok=True)

    write_json(LOCK_PATH, lock)
    write_marketplace()
    write_notices(lock)
    write_readme_table()


def write_marketplace() -> None:
    m = STACK["marketplace"]
    entries = []
    for local in STACK["local_plugins"]:
        entries.append({
            "name": local["plugin"],
            "source": f"./plugins/{local['plugin']}",
            "description": local["description"],
            "author": m["owner"],
            "category": local["category"],
            "license": "MIT",
            "homepage": m["repository"],
            "keywords": KEYWORDS,
        })
    for src in STACK["sources"]:
        if src.get("reference_only"):
            continue
        entries.append({
            "name": src["plugin"],
            "source": f"./plugins/{src['plugin']}",
            "description": src["description"],
            "author": {"name": src["author"]},
            "category": src["category"],
            "license": src["license"],
            "homepage": src.get("homepage", f"https://github.com/{src['repo']}"),
            "keywords": KEYWORDS,
        })
    write_json(ROOT / ".claude-plugin" / "marketplace.json", {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": m["name"],
        "owner": m["owner"],
        "metadata": {"description": m["description"]},
        "plugins": entries,
    })


def write_notices(lock: dict) -> None:
    out = [
        "# Third-party notices",
        "",
        "This repository redistributes selected skills and reference prompts below,",
        "each under its original license. The license file of every project is copied",
        "into its plugin folder or the listed reference directory. Original router,",
        "owned ELI5 style, scripts, and documentation are MIT; see [LICENSE](LICENSE).",
        "Adapted styles and copied references retain the upstream grants below.",
        "",
        "_Generated by `scripts/sync.py`, do not edit by hand._",
        "",
    ]
    for src in STACK["sources"]:
        info = lock[src["id"]]
        out += [
            f"## {src['id']} — `plugins/{src['plugin']}`",
            "",
            f"- Upstream: https://github.com/{src['repo']} @ `{info['commit']}`",
            f"- Author: {src['author']}",
            f"- License: {src['license']} (see `plugins/{src['plugin']}/"
            f"{src.get('license_dir', '').rstrip('/') + '/' if src.get('license_dir') else ''}"
            f"{Path(src['license_files'][0]).name}`)",
        ]
        out.append("- Preserved license/notice files: " + ", ".join(f"`{name}`" for name in src["license_files"]))
        if src.get("reference_only"):
            out.append("- Packaging: reference-only copies inside the owned plugin; no installer or registered skill.")
        for item in src["copy"]:
            if item.get("plugin", src["plugin"]) != src["plugin"]:
                out.append(f"- Cached adapter notice copy: `plugins/{item['plugin']}/{item['to']}` (verbatim).")
        patches = src.get("patches", [])
        if patches:
            out.append("- Modifications: these files were patched for task scope and conflict rulings;"
                       " everything else is copied verbatim.")
            out += [f"  - `{p['file']}`: {p['why']}" for p in patches]
        else:
            out.append("- Modifications: none, copied verbatim.")
        for adaptation in src.get("adaptations", []):
            out.append(f"- Adaptation: `{adaptation['file']}` — {adaptation['why']}")
        out.append("")
    (ROOT / "THIRD_PARTY_NOTICES.md").write_text("\n".join(out))


def all_skills() -> list[tuple[str, Path, dict[str, str]]]:
    found = []
    for plugin in sorted(p for p in PLUGINS.glob("*") if p.is_dir()):
        for skill_md in sorted(plugin.rglob("SKILL.md")):
            if "tests" in skill_md.relative_to(plugin).parts:
                continue
            found.append((plugin.name, skill_md, frontmatter(skill_md.read_text())))
    return found


def write_readme_table() -> None:
    order = [p["plugin"] for p in STACK["local_plugins"]] + [s["plugin"] for s in STACK["sources"] if not s.get("reference_only")]
    by_plugin: dict[str, list[str]] = {}
    for plugin, _, fm in all_skills():
        by_plugin.setdefault(plugin, []).append(fm.get("name", "?"))
    total = sum(len(v) for v in by_plugin.values())
    rows = ["| Plugin | Skills | Count |", "|---|---|---|"]
    for plugin in order:
        names = by_plugin.get(plugin, [])
        rows.append(f"| `{plugin}` | {', '.join(f'`{n}`' for n in names)} | {len(names)} |")
    rows.append(f"| **Total** | | **{total}** |")
    block = "<!-- SKILLS:START -->\n" + "\n".join(rows) + "\n<!-- SKILLS:END -->"
    for name in ("README.md", "README.pt-BR.md"):
        readme = ROOT / name
        if readme.exists():
            localized = block.replace("| Plugin | Skills | Count |", "| Plugin | Skills | Quantidade |") if name.endswith("pt-BR.md") else block
            text = readme.read_text()
            new = re.sub(r"<!-- SKILLS:START -->.*?<!-- SKILLS:END -->", localized, text, flags=re.S)
            readme.write_text(new)


def check() -> int:
    errors: list[str] = []
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    for entry in market["plugins"]:
        pdir = ROOT / entry["source"]
        if not (pdir / ".claude-plugin" / "plugin.json").exists():
            errors.append(f"{entry['name']}: missing .claude-plugin/plugin.json")
    names: dict[tuple[str, str], Path] = {}
    for plugin, skill_md, fm in all_skills():
        if not fm.get("name") or not fm.get("description"):
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter needs name and description")
            continue
        key = (plugin, fm["name"])
        if key in names:
            errors.append(f"duplicate skill {fm['name']} in {plugin}")
        names[key] = skill_md
    for e in errors:
        print(f"error: {e}")
    print(f"checked {len(market['plugins'])} plugins, {len(names)} skills, {len(errors)} errors")
    return 1 if errors else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, help="directory with pre-cloned upstreams (<owner>_<repo>)")
    ap.add_argument("--check", action="store_true", help="validate only")
    args = ap.parse_args()
    if args.check:
        return check()
    sync(args.src.resolve() if args.src else None)
    return check()


if __name__ == "__main__":
    sys.exit(main())
