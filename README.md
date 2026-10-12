# 🧮 Operações com Conjuntos em Python

Programa de menu interativo que implementa operações com conjuntos **sem usar os operadores nativos do Python**, validando os resultados contra a solução nativa (`set`).

Trabalho acadêmico da disciplina de [NOME DA DISCIPLINA] — [NOME DA FACULDADE].

## 📌 Objetivo

Implementar manualmente (com laços `for` e condicionais `if`) as principais operações da teoria dos conjuntos e comparar cada resultado com a solução nativa da linguagem, garantindo o aprendizado dos conceitos.

## ⚙️ Operações Implementadas

| Operação | Notação | Implementação manual | Solução nativa |
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

## 🧠 Estratégia

Todas as operações foram construídas usando **apenas**:

- Estruturas de repetição (`for`)
- Estruturas condicionais (`if` / `else`)
- A função auxiliar `pertence()`, que **substitui o operador `in`**

Nenhum operador nativo de conjunto (`|`, `&`, `-`, `^`, `in`, `issubset`, etc.) foi usado na implementação manual.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior

### Passos

```bash
# Clone o repositório
git clone https://github.com/SEU-USUARIO/operacoes-conjuntos.git

# Entre na pasta
cd operacoes-conjuntos

# Execute o programa
python conjuntos.py
```

## 🖥️ Como Usar

1. Ao iniciar, digite os elementos dos conjuntos **A** e **B** separados por espaço.
2. Para conjunto vazio, apenas aperte **Enter**.
3. Escolha a operação desejada no menu.
4. O programa exibirá **lado a lado** a implementação manual e a solução nativa, indicando se são iguais (✅) ou diferentes (❌).

### Exemplo de execução

```
Digite os elementos de A separados por espaço: 1 2 3 4
Digite os elementos de B separados por espaço: 3 4 5 6

================ MENU ================
1 - União (A ∪ B)
2 - Interseção (A ∩ B)
...
Escolha: 1

--- União ---
  Implementação manual: ['1', '2', '3', '4', '5', '6']
  Solução nativa (set): {'1', '2', '3', '4', '5', '6'}
  Iguais? ✅ SIM
```

## 🧪 Casos de Teste

Foram realizadas **três execuções** cobrindo cenários distintos:

### Execução 1 — Conjuntos com elementos em comum
- **A:** `1 2 3 4`
- **B:** `3 4 5 6`
- **Resultado:** todas as operações bateram com a solução nativa ✅

### Execução 2 — Conjunto vazio
- **A:** *(vazio)*
- **B:** `10 20 30`
- **Resultado:** união, interseção e diferenças conferiram ✅

### Execução 3 — Conjuntos iguais e disjuntos

**3a — Iguais:**
- **A:** `a b c`
- **B:** `a b c`
- Diferença simétrica = vazio ✅

**3b — Disjuntos:**
- **A:** `1 2`
- **B:** `x y`
- Interseção = vazio ✅

## 📁 Estrutura do Projeto

```
operacoes-conjuntos/
├── conjuntos.py     # Código-fonte principal
├── README.md        # Este arquivo
└── .gitignore       # Arquivos ignorados pelo Git
```

## 🛠️ Tecnologias

- **Python 3** — linguagem única do projeto
- Nenhuma biblioteca externa necessária

## 👤 Autor

**[SEU NOME COMPLETO]**
- GitHub: [@SEU-USUARIO](https://github.com/SEU-USUARIO)
- E-mail: seu.email@exemplo.com

## 📜 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.