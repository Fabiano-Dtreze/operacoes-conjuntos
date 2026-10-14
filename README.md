# Operações com Conjuntos em Python

Programa que implementa operações com conjuntos **sem usar operadores nativos**, validando contra a solução nativa.

Trabalho acadêmico — Matemática para Computação — Fatec Osasco.

## Objetivo

Implementar manualmente as operações da teoria dos conjuntos com laços e condicionais, comparando com a solução nativa.

## Operações Implementadas

| Operação | Manual | Nativo |
|---|---|---|
| Pertinência | `pertence(x, A)` | `x in setA` |
| União | `uniao(A, B)` | `setA \| setB` |
| Interseção | `interseccao(A, B)` | `setA & setB` |
| Diferença | `diferenca(A, B)` | `setA - setB` |
| Dif. Simétrica | `diferenca_simetrica(A, B)` | `setA ^ setB` |
| Inclusão | `esta_contido(A, B)` | `setA.issubset(setB)` |
| Cardinalidade | `cardinalidade(A)` | `len(setA)` |
| Complemento | `complemento(A, U)` | `set(U) - setA` |

## Como Executar

```bash
