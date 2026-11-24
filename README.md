# Estruturas de Dados em Python

Implementações de estruturas de dados clássicas em Python, feitas do zero (sem bibliotecas prontas) e aplicadas a problemas práticos.

> Atividades da disciplina **Consultoria Especializada de Apoio ao Projeto Integrado: Estrutura de Dados e Programação**, do Bacharelado em Ciência de Dados e Inteligência Artificial da **PUC-SP** (2025/2).

## Conteúdo

| # | Arquivo | Estrutura | Aplicação |
|---|---|---|---|
| 1 | [`01_pilha_validador_html.ipynb`](01_pilha_validador_html.ipynb) | Pilha (LIFO) | Verifica se as tags de um HTML abrem e fecham na ordem correta |
| 2 | [`02_fila_assincrona_atendimento.ipynb`](02_fila_assincrona_atendimento.ipynb) | Fila (FIFO) + `asyncio` | Simulação de atendimento que ajusta o número de atendentes conforme a fila cresce |
| 3 | [`03_fila_de_prioridade.ipynb`](03_fila_de_prioridade.ipynb) | Fila de prioridade (ordenada e não ordenada) | Comparação de custos + Selection Sort e Insertion Sort |
| 4 | [`04_lista_duplamente_encadeada.ipynb`](04_lista_duplamente_encadeada.ipynb) | Lista duplamente encadeada | Pilha e Fila construídas sobre a lista |
| 5 | [`05_arvore_binaria_busca.py`](05_arvore_binaria_busca.py) | Árvore binária de busca (BST) | Reconstrói a árvore a partir da pré-ordem e imprime a pós-ordem |

## Destaques

**Validador de HTML com pilha.** Cada tag de abertura é empilhada; cada tag de fechamento precisa corresponder ao topo da pilha. Trata tags auto-fechadas (`<br/>`, `<img/>`) e ignora atributos.

```python
verificar_html("<html><body><h1>Título</h1></body></html>")  # True
verificar_html("<b><i>Texto</b></i>")                         # False (ordem errada)
```

**Simulação de atendimento assíncrona.** Três tarefas rodam em paralelo com `asyncio`: chegada de clientes, atendimento e um monitor que **adiciona atendentes quando a fila passa de 10 pessoas** e remove quando fica ociosa. Um `asyncio.Lock` evita conflitos de acesso à fila.

```
o tamanho da fila é de 13 pessoas.
adicionando um atendente......total =  2 atendentes
...
Simulação encerrada: 21 pessoas na fila e 4 atendente(s).
```

**Fila de prioridade: o trade-off.**

| Implementação | Inserir | Achar o mínimo |
|---|---|---|
| Não ordenada | O(1) | O(n) |
| Ordenada | O(n) | O(1) |

## Como executar

Os notebooks rodam no Jupyter ou no Google Colab (Python 3.10+). A simulação assíncrona usa `nest_asyncio`:

```bash
pip install nest_asyncio
```

A árvore binária roda pelo terminal:

```bash
python 05_arvore_binaria_busca.py < exemplo_entrada.txt
# 5 28 24 45 30 60 52 98 50
```

## Tecnologias

Python · Programação orientada a objetos · `asyncio` · Jupyter Notebook

## Autora

**Giovanna Freitas**, estudante de Ciência de Dados e IA na PUC-SP.
[LinkedIn](https://www.linkedin.com/in/giovanna-freitas-a36899353)
