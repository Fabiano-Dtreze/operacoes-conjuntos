# Operações com Conjuntos em Python

Programa que implementa operações com conjuntos **sem usar operadores nativos**, validando contra a solução nativa do Python.

Trabalho acadêmico — Matemática para Computação — Fatec Osasco.

---

## Objetivo

Implementar manualmente (com laços e condicionais) as operações da teoria dos conjuntos e comparar cada resultado com a solução nativa da linguagem.

---

## Operações Implementadas

| Operação | Notação | Implementação Manual | Solução Nativa |
|---|---|---|---|
| Pertinência | x ∈ A | `pertence(x, A)` | `x in setA` |
| União | A ∪ B | `uniao(A, B)` | `setA \| setB` |
| Interseção | A ∩ B | `interseccao(A, B)` | `setA & setB` |
| Diferença | A − B | `diferenca(A, B)` | `setA - setB` |
| Diferença | B − A | `diferenca(B, A)` | `setB - setA` |
| Diferença Simétrica | A △ B | `diferenca_simetrica(A, B)` | `setA ^ setB` |
| Inclusão | A ⊆ B | `esta_contido(A, B)` | `setA.issubset(setB)` |
| Inclusão | A ⊇ B | `contem(A, B)` | `setA.issuperset(setB)` |
| Cardinalidade | \|A\| | `cardinalidade(A)` | `len(setA)` |
| Complemento | ∁ᵁA | `complemento(A, U)` | `set(U) - setA` |

---

## Decisões de Projeto

**Por que implementar manualmente?**
O objetivo do trabalho era compreender a teoria dos conjuntos por dentro, não apenas usar funções prontas. Cada operação foi construída do zero com `for` e `if`.

**Por que comparar com a solução nativa?**
Para validar automaticamente que a implementação manual está correta. Se os dois resultados coincidem, a lógica está correta.

**Por que usar listas em vez de sets?**
Para forçar a implementação manual das operações. Se usássemos `set` diretamente, o Python aplicaria as operações prontas automaticamente.

---

## Como Executar

Pré-requisitos: Python 3.8 ou superior.

```bash
git clone https://github.com/Fabiano-Dtreze/operacoes-conjuntos.git
cd operacoes-conjuntos
python conjuntos.py
