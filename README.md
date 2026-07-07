# Assembler Hack (Nand2Tetris — Project 6)

**Atividade Avaliativa para a disciplina Compiladores do curso Bacharel em Engenharia da Computação na Universidade Federal do Maranhão, ministrada pelo Profº Drº Sergio Souza Costa.**

## Dupla

* **André Luis Aguiar do Nascimento** — 20250071151
* **Virginia Maria Mondego Ferreira** — 20250071349

## Linguagem e Versão

* **Linguagem:** Python 3.11+
* **Justificativa da Escolha:** A escolha do Python baseia-se na sua excelente capacidade de manipulação de strings e Expressões Regulares, o que simplifica drasticamente a etapa de tokenização e limpeza de comentários do *Parser*. Além disso, o uso de dicionários nativos permite um mapeamento direto, limpo e performático para as tabelas de tradução binária (instruções C), criando um código modular, legível e de fácil manutenção.

---

## Estrutura do Repositório

```text
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
│   ├── test_code.py       
│   └── test_integration.py  
├── projects/06/           
├── out/  # caso tenha rodado o comando                 
├── README.md
└── .gitignore
```

## Instruções de Execução

Para rodar o assembler e traduzir um arquivo de código assembly (`.asm`) para binário máquina (`.hack`), execute o orquestrador a partir do diretório raiz do projeto utilizando o terminal:

```bash
python main/assembler.py <caminho_do_arquivo.asm>
```

O programa criará automaticamente um diretório chamado out/ na raiz do projeto e salvará o arquivo traduzido lá dentro.

## Exemplos de Uso

Abaixo estão os comandos para executar a tradução de todos os arquivos de teste oficiais do projeto:

```
# Exemplo 1: Traduzir o arquivo Add (Obrigatório)
python main/assembler.py projects/06/add/Add.asm
# Saída gerada: out/Add.hack

# Exemplo 2: Traduzir o arquivo Max com Labels (Obrigatório)
python main/assembler.py projects/06/max/Max.asm
# Saída gerada: out/Max.hack

# Exemplo 3: Traduzir o arquivo Rect (Recomendado)
python main/assembler.py projects/06/rect/Rect.asm
# Saída gerada: out/Rect.hack

# Exemplo 4: Traduzir o arquivo Pong (Desafio Opcional)
python main/assembler.py projects/06/pong/Pong.asm
# Saída gerada: out/Pong.hack
```

## Vídeo de Apresentação

O vídeo demonstrando o funcionamento interno do código, a estratégia de duas passagens e a validação das saídas geradas no CPU Emulator pode ser assistido através do link abaixo:

[drive.google.com/file/d/1G4iv1-ABJvWe21blKY-msBgPqkz_af6s/view?usp=sharing](https://drive.google.com/file/d/1G4iv1-ABJvWe21blKY-msBgPqkz_af6s/view?usp=sharing)
