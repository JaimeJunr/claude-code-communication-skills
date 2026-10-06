# Claude Code Communication Skills (pt-BR)

**Respostas objetivas, curtas e claras, sem desvio de assunto.** Um marketplace
reúne receitas de comunicação existentes, resolve suas regras conflitantes e
oferece quatro estilos opcionais. Preserva significado, voz do autor, conteúdo
técnico exato e rigor de engenharia.

[English](README.md)

## Por que existe

Uma receita de brevidade pode prejudicar a gramática; uma simplificação pode
apagar ressalvas; um editor pode substituir a voz pessoal. Empilhar todos também
acrescenta instruções concorrentes e custo de contexto. A stack escolhe uma
receita por tarefa, separa conversa, prosa publicável e texto de máquina, e não
inclui hooks.

A pesquisa está em [DESIGN.md](docs/research/DESIGN.md) e
[ANALYSIS.md](docs/research/ANALYSIS.md). O layout segue o marketplace frontend
vizinho: um plugin por upstream, mais o plugin de integração.

## O que entra e por quê

- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman): somente a
  skill base, para uma passagem de brevidade solicitada. Gramática legível,
  incerteza real e escopo por tarefa substituem o modo persistente. Apache-2.0;
  preserva `LICENSE`, `NOTICE`, `LICENSE-MIT` e `LICENSING.md`.
- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd): resposta ou ação
  primeiro, passos delimitados, progresso útil e cobertura completa. Só a skill
  canônica; nenhum hook always-on. MIT.
- [blader/humanizer](https://github.com/blader/humanizer): reescrita substancial
  de prosa fornecida, mantendo afirmações sustentadas e a amostra do autor.
  O corpo completo só carrega para a tarefa escolhida. MIT.
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop): edição
  mínima de rascunhos e auditoria de padrões sem reescrita. Mantém o
  `eval.md` obrigatório ao lado da skill. MIT.
- [rahulj51/eli5](https://github.com/rahulj51/eli5): explicações executivas ou
  em linguagem simples e Simplified Technical English solicitado explicitamente.
  O plugin se chama `eli5-ste`. MIT.
- [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal): o prompt
  compacto é adaptado no Stack Clear. Os dois prompts originais e a licença
  MIT ficam como referências no plugin próprio. Nenhum instalador ou skill
  talk-normal é registrado.

O plugin **communication-stack** contém o roteador, a precedência, os conflitos
e quatro estilos. O estilo **ELI5 é o arquivo escrito pelo usuário**, exatamente
a versão corrigida na seção B de DESIGN.md. É diferente da receita
`eli5-ste:eli5` de Rahul.

<!-- SKILLS:START -->
| Plugin | Skills | Quantidade |
|---|---|---|
| `communication-stack` | `communication-stack` | 1 |
| `caveman` | `caveman` | 1 |
| `i-have-adhd` | `i-have-adhd` | 1 |
| `humanizer` | `humanizer` | 1 |
| `no-ai-slop` | `no-ai-slop` | 1 |
| `eli5-ste` | `eli5`, `ste` | 2 |
| **Total** | | **7** |
<!-- SKILLS:END -->

## Instalar

Depois da publicação deste repositório, execute no Claude Code:

```text
/plugin marketplace add JaimeJunr/claude-code-communication-skills
/plugin install communication-stack@communication-stack
/plugin install caveman@communication-stack
/plugin install i-have-adhd@communication-stack
/plugin install humanizer@communication-stack
/plugin install no-ai-slop@communication-stack
/plugin install eli5-ste@communication-stack
```

Os plugins são independentes. Instalar só `communication-stack` fornece os
quatro estilos. Instale os upstreams necessários ao roteador; se a fonte
escolhida estiver indisponível, ele informa qual falta sem trocar de editor
silenciosamente.

Remova cópias duplicadas instaladas dos repositórios originais. Na migração,
confira uma vez os hooks de caveman/ADHD, estilos forçados e blocos antigos de
talk-normal no AGENTS.md. Este marketplace não examina nem altera essas outras
instalações automaticamente.

### Em um projeto de equipe

Coloque isto em `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "communication-stack": {
      "source": {
        "source": "github",
        "repo": "JaimeJunr/claude-code-communication-skills"
      }
    }
  },
  "enabledPlugins": {
    "communication-stack@communication-stack": true,
    "caveman@communication-stack": true,
    "i-have-adhd@communication-stack": true,
    "humanizer@communication-stack": true,
    "no-ai-slop@communication-stack": true,
    "eli5-ste@communication-stack": true
  }
}
```

Ligado não significa instalado. Cada máquina precisa da própria instalação:

```bash
for p in communication-stack caveman i-have-adhd humanizer no-ai-slop eli5-ste; do
  claude plugin install "$p@communication-stack" --scope project
done
claude plugin list
```

Abra uma sessão nova depois da instalação.

## Escolher um estilo

Use `/output-style` para listar os estilos ou `/config` → **Output style**:

- **Stack Clear**: conversa comum, resposta direta, contexto útil e fim sem
  repetição. Ponto de partida recomendado.
- **ELI5**: palavras simples, respostas curtas, definições logo após termos
  difíceis e o mesmo rigor técnico. Os campos de relatório só valem para
  trabalho realizado; pedidos mais amplos superam a preferência por duas opções.
- **Stack ADHD**: resposta ou ação primeiro, passos numerados delimitados,
  progresso útil e grupos pequenos sem apagar itens necessários.
- **Stack Caveman Lite**: brevidade experimental com gramática completa e
  legível. É o nome da nossa adaptação; os aliases atuais lite/full do upstream
  usam a mesma skill base.

Todos mantêm `keep-coding-instructions: true` e `force-for-plugin: false`.
Ativar o plugin respeita o estilo já selecionado. O manifesto usa a descoberta
padrão em `output-styles/` e omite `outputStyles`, que substituiria essa busca.
Veja a [documentação de estilos](https://code.claude.com/docs/en/output-styles)
e a [referência do manifesto](https://code.claude.com/docs/en/plugins-reference).

Se também mantiver `~/.claude/output-styles/eli5.md` com o nome **ELI5**, renomeie
o `name` de um dos estilos para evitar ambiguidade.

## Usar as receitas

Peça uma transformação; o roteador escolhe uma receita principal:

| Pedido | Receita |
|---|---|
| Editar um rascunho mantendo minha voz | `no-ai-slop:no-ai-slop` |
| Reescrever substancialmente prosa com padrões artificiais | `humanizer:humanizer` |
| Auditar padrões sem reescrever | `no-ai-slop:no-ai-slop`, modo detect |
| Versão simples ou executiva de conteúdo específico | `eli5-ste:eli5` |
| Simplified Technical English explicitamente solicitado | `eli5-ste:ste` |
| Formatação com ação primeiro nesta tarefa | `i-have-adhd:i-have-adhd` |
| Passagem de brevidade nesta tarefa | `caveman:caveman` |

Também pode chamar `/no-ai-slop:no-ai-slop`, `/humanizer:humanizer` ou
`/eli5-ste:eli5` diretamente. Uma fonte pedida pelo usuário supera o padrão.

As seis receitas continuam invocáveis pelo modelo, com descrições restritas:
carregam apenas por pedido explícito ou quando o roteador communication-stack
seleciona uma delas. O roteador chama a skill pelo nome com namespace usando a
ferramenta Skill e carrega somente essa receita. Nunca invoque mais de um editor
por tarefa. Se o plugin não estiver instalado, informe isso e dê
`/plugin install <name>@communication-stack`.

A receita vale apenas para a tarefa ou artefato atual. Não muda o estilo
selecionado nem governa tarefas posteriores. Conversas comuns, code reviews e
trabalho de engenharia não carregam editores só por produzirem prosa.

## Regras de conflito

- **Conversa:** pedido/idioma/contrato de saída atual → receita da tarefa →
  estilo selecionado → brevidade genérica.
- **Prosa publicável:** briefing/público/contrato → amostra e voz do autor →
  um editor → padrões do editor.
- **Texto de máquina:** esquema/sintaxe/contrato literal → convenções do projeto
  para conteúdo novo. O estilo só muda a prosa ao redor.

Os dez julgamentos exigem resposta primeiro, gramática legível, conteúdo acima
de limites, fim no mesmo objetivo, progresso com estado alterado, listas reais
completas, voz e desvios intencionais preservados, avaliação contextual de
padrões, texto final uma vez e conteúdo de máquina exato. Ressalvas e contrastes
informativos sobrevivem. Detect retorna evidências sem inferir autoria.

Veja os dez em
[conflicts.md](plugins/communication-stack/skills/communication-stack/references/conflicts.md)
e o [registro dos 44 conflitos](docs/research/DESIGN.md#complete-register-of-all-44-audited-conflicts).

## O que fica de fora e por quê

- **hardikpandya/stop-slop:** duplica os editores; proibições absolutas de
  advérbios, atores, voz passiva, pontuação e quantidade de itens exigem reparos
  grandes.
- **obra/the-elements-of-style:** não há licença do repositório cobrindo o
  wrapper moderno; o texto histórico de Strunk em domínio público não resolve isso.
- **Kyaa-A/eli5:** prioriza simplicidade sobre precisão, esconde ressalvas e
  impõe cinco frases.
- **fcakyon ADHD:** estilo forçado e blocos Insight obrigatórios conflitam com
  seleção opcional, respostas curtas e artefatos sem comentários.
- **smixs/awesome-claude-output-styles:** referência derivada de empacotamento;
  fontes diretas evitam outra camada de upstream e presets sobrepostos.
- **As outras 21 skills de caveman:** `ultracave`, `megacave`,
  `caveman-compress`, `caveman-commit`, `caveman-review`, `cavecrew`,
  `caveman-discover`, `caveman-evidence-review`, `caveman-explore`,
  `caveman-help`, `caveman-learn`, `caveman-manage`, `caveman-optimize`,
  `caveman-setup`, `caveman-stats`, `investigate-first`, `lean-build`,
  `migration`, `safe-refactor`, `surgical-patch` e `verify-and-stop`.
  Removem gramática, trocam idioma, alteram memória ou acrescentam políticas de
  artefatos, programação, delegação e Cloud fora deste escopo.
- **Todos os hooks, instaladores e mecanismos de runtime:** nenhuma injeção de
  início de sessão, flag always-on, reescrita automática, oferta de statusline
  ou alteração de AGENTS.md.

## Sincronização

[stack.json](stack.json) lista seis fontes em `ref: main`, caminhos, licenças
e patches. [scripts/sync.py](scripts/sync.py) gera os cinco plugins upstream,
referências talk-normal, marketplace, avisos, lock e tabelas dos READMEs.
Os demais arquivos do plugin próprio sobrevivem, incluindo o ELI5 exato.
Os outros três estilos são mantidos à mão e revistos após atualizações.

`reference_only` copia talk-normal diretamente para as referências do roteador,
preservando os arquivos próprios e sem criar outro plugin vazio. Os prompts
ficam junto da adaptação, dentro do pacote instalado.

Entradas `copy` com outro `plugin` também preservam licenças e avisos de caveman
e ADHD nas referências do plugin próprio, mantendo suas concessões mesmo quando
ele é instalado sozinho. Essas referências geradas são os únicos destinos extras.

[UPSTREAM.lock](UPSTREAM.lock) guarda seis SHAs completos, licenças e hashes
SHA-256 dos arquivos originais antes dos patches. Os corpos originais podem
ser consultados nesses commits, sem árvore vendor duplicada. Cada patch
registra commit revisado, motivo e conflitos; mudança de contexto ou quantidade
de correspondências interrompe o sync. Alterações de licença/NOTICE pedem revisão.

```bash
python scripts/sync.py
python scripts/sync.py --src .cache/upstream
python scripts/sync.py --check
```

`--src` usa clones `<owner>_<repo>` no HEAD existente, sem buscar na rede.
Clone ausente causa erro. Repetir com os mesmos seis clones limpos reproduz os
bytes gerados, inclusive as datas do lock.

A Action semanal roda segunda-feira às 09:00 UTC e abre um PR. Configure
`SYNC_TOKEN` com acesso de escrita a Contents e Pull requests. PRs abertos com
o `GITHUB_TOKEN` padrão não disparam a validação; use `SYNC_TOKEN` para exigir
esse check antes do merge.

## Avaliação TODO

Os testes validam a estrutura; a avaliação de comportamento **não foi rodada**.
Implementar a [seção E de DESIGN.md](docs/research/DESIGN.md#e-biggest-risk-and-cheap-evaluation):

- [ ] Fixar **20 casos**: 6 conversas curtas, 4 diálogos com vários turnos,
  4 explicações, 3 textos publicáveis e 3 casos de texto de máquina. Definir
  fatos esperados, trechos protegidos e cobertura antes da pontuação. Incluir
  uma tarefa posterior não relacionada para detectar vazamento de escopo.
- [ ] Comparar Default, Concise nativo, Stack Clear e ELI5 próprio com o mesmo
  modelo, parâmetros, ferramentas e orçamento: **80 execuções**. Acrescentar
  **5 casos pareados por estilo** para Stack ADHD e Stack Caveman Lite:
  **90 execuções iniciais**, mais os turnos previstos. Repetir só resultados
  ambíguos.
- [ ] Medir mediana e maior resposta em palavras por conversa/artefato, resposta
  primeiro, desvio de objetivo, completude/precisão, bytes protegidos, contrato
  final-only, receita escolhida e avaliação humana cega de voz/legibilidade.
  Registrar tokens reais de entrada/saída, contexto posterior, cache, latência
  e custo de roteamento/carregamento.
- [ ] Buscar 90% de resposta primeiro, 95% sem desvio e zero falhas de conteúdo
  obrigatório, fatos inventados, trechos protegidos ou contrato do artefato.
  Menos palavras em conversa que Default; comparar Concise separadamente.
  Igualar sua legibilidade, preservar voz e impedir colisão ou modo persistente.
- [ ] Rodar duas pequenas tarefas de engenharia com as instruções e verificações
  do projeto antes da publicação. Corrigir ou retirar estilos que prejudiquem
  significado, exatidão ou leitura.

São metas dessa suíte pequena, não taxas gerais medidas. Menos palavras de
saída não provam economia total de tokens.

## Contribuir e licenças

Veja [CONTRIBUTING.md](CONTRIBUTING.md). O roteador original, o ELI5 próprio,
scripts e documentação são MIT, copyright Jaime Basso. Receitas, referências
e estilos adaptados mantêm suas licenças upstream. Fontes, avisos preservados
e alterações estão em [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
