# Hack Assembler

Projeto do assembler Hack do Nand2Tetris, Project 6.

## Estrutura

```text
assembler/
├── parser/
├── symbol_table/
├── code/
├── main/
├── tests/
└── projects/06/
```

## Módulos: parser e symbol_table

### Parser

O módulo `parser` lê arquivos `.asm`, remove comentários e linhas em branco, mantém a instrução atual e expõe os métodos esperados para percorrer e decompor instruções Hack:

- `hasMoreInstructions()`
- `advance()`
- `instructionType()`
- `symbol()`
- `dest()`
- `comp()`
- `jump()`
- `reset()`

Tipos retornados por `instructionType()`:

- `A_INSTRUCTION`, para instruções como `@2` e `@R0`
- `C_INSTRUCTION`, para instruções como `D=M`, `D;JGT` e `0;JMP`
- `L_INSTRUCTION`, para labels como `(LOOP)`

### SymbolTable

O módulo `symbol_table` inicializa a tabela de símbolos com os símbolos predefinidos da plataforma Hack:

- `SP`, `LCL`, `ARG`, `THIS`, `THAT`
- `R0` até `R15`
- `SCREEN`
- `KBD`

Também oferece os métodos:

- `addEntry(symbol, address)`, para labels e símbolos com endereço conhecido
- `addVariable(symbol)`, para variáveis alocadas a partir do endereço 16
- `contains(symbol)`
- `getAddress(symbol)`

## Testes

Execute:

```bash
python3 -m unittest discover -s tests
```


