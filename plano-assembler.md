# Plano de Desenvolvimento — Assembler Hack (Nand2Tetris Project 6)

**Dupla:** André & Virginia
**Linguagem:** Python 3 (ajustável)
**Estratégia:** André constrói a base (Parser + SymbolTable) → Virginia constrói em cima (Code + Main + Testes + Vídeo)

---

## 1. Estrutura do repositório

```
assembler/
├── parser/
│   └── parser.py
├── symbol_table/
│   └── symbol_table.py
├── code/
│   └── code.py
├── main/
│   └── assembler.py
├── tests/
│   ├── test_parser.py
│   ├── test_symbol_table.py
│   └── test_code.py
├── projects/06/        # arquivos .asm de teste (add, max, maxL, rect, pong)
├── README.md
└── .gitignore
```

## 2. Branches

| Branch                        | Responsável                       | Base                                  |
| ----------------------------- | ---------------------------------- | ------------------------------------- |
| `main`                      | protegida, só recebe merge via PR | —                                    |
| `feature/setup`             | André                             | main                                  |
| `feature/parser`            | André                             | main                                  |
| `feature/symbol-table`      | André                             | main                                  |
| `feature/code-generator`    | Virginia                           | main (após merge do André)          |
| `feature/main-orchestrator` | Virginia                           | main (após merge do código gerador) |
| `feature/tests-integration` | Virginia                           | main                                  |
| `feature/video-docs`        | Virginia                           | main                                  |

**Fluxo:** André abre PR de `feature/setup`, `feature/parser` e `feature/symbol-table` → merge em `main`. Só então Virginia cria suas branches a partir do `main` atualizado, para já ter o Parser e a SymbolTable prontos.

---

## 3. Parte 1 — André (Parser + SymbolTable)

### `feature/setup` (1 commit)

1. `chore: cria estrutura de pastas e .gitignore`

### `feature/parser` (5 commits)

2. `feat(parser): implementa leitura do arquivo .asm e remoção de comentários/espaços`
3. `feat(parser): implementa hasMoreInstructions e advance`
4. `feat(parser): implementa instructionType (A_INSTRUCTION, C_INSTRUCTION, LABEL)`
5. `feat(parser): implementa symbol(), dest(), comp() e jump()`
6. `test(parser): adiciona testes unitários do parser (add.asm, maxL.asm)`

### `feature/symbol-table` (3 commits)

7. `feat(symbol_table): inicializa tabela com símbolos predefinidos (R0-R15, SP, SCREEN, KBD...)`
8. `feat(symbol_table): implementa addEntry, addVariable e getAddress`
9. `test(symbol_table): testes unitários (labels e variáveis a partir do endereço 16)`

**Total André: 9 commits** (mínimo 8 ✅)

**Entrega do André:** Parser e SymbolTable funcionando isoladamente, com testes passando, documentados no README (seção "Módulos: parser e symbol_table"), e PR mergeado em `main`.

---

## 4. Parte 2 — Virginia (Code + Main + Testes + Vídeo)

Parte da branch `main` já com Parser/SymbolTable prontos.

### `feature/code-generator` (4 commits)

1. `feat(code): implementa encode_a_instruction`
2. `feat(code): adiciona tabelas COMP_TABLE, DEST_TABLE, JUMP_TABLE`
3. `feat(code): implementa encode_c_instruction (comp+dest+jump)`
4. `test(code): testes unitários do gerador de código binário`

### `feature/main-orchestrator` (2 commits)

5. `feat(main): implementa primeira passagem (coleta de labels)`
6. `feat(main): implementa segunda passagem (resolve variáveis e gera .hack)`

### `feature/tests-integration` (2 commits)

7. `test(integration): valida add.asm e max.asm no CPU Emulator`
8. `test(integration): valida maxL.asm e rect.asm (pong.asm como desafio opcional)`

### `feature/video-docs` (2 commits)

9. `docs(readme): instruções de build, execução e exemplos de uso`
10. `docs(readme): adiciona link do vídeo de apresentação`

**Total Virginia: 10 commits** (mínimo 8 ✅)

---

## 5. Vídeo de apresentação (responsabilidade compartilhada, roteiro já vem no enunciado)

Como o Main e os testes de integração são da Virginia, faz sentido ela puxar a gravação, mas os dois devem aparecer e falar:

- **0:00–1:00** — Abertura (ambos)
- **1:00–4:00** — Arquitetura (André explica parser/symbol_table)
- **4:00–8:00** — Demonstração técnica (Virginia roda add.asm/max.asm no CPU Emulator)
- **8:00–12:00** — Detalhes de implementação (ambos: André fala de duas passagens/labels, Virginia fala de encoding)
- **12:00–15:00** — rect.asm/pong.asm, conclusão e lições aprendidas (ambos)

---

## 6. Ordem sugerida de execução

1. André: setup do repo + parser + symbol_table → PR → merge
2. Virginia: puxa `main`, cria code_generator sobre o parser/symbol_table prontos
3. Virginia: main orchestrator (duas passagens) usando Code + Parser + SymbolTable
4. Virginia: roda os testes de integração no CPU Emulator
5. Ambos: gravam o vídeo
6. Virginia: fecha o README com instruções finais e link do vídeo
7. Revisão final conjunta antes da entrega

## 7. Checklist de entrega

- [ ] Repositório `assembler` com histórico de commits ≥ 6 (vocês terão ~19 no total)
- [ ] README com nomes, RA, linguagem, build/execução, exemplos
- [ ] add.asm e max.asm traduzidos corretamente (obrigatório)
- [ ] rect.asm traduzido (recomendado)
- [ ] pong.asm traduzido (opcional/desafio)
- [ ] Vídeo ≤ 15 min, link no README
