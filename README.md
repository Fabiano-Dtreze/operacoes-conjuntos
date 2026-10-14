# ☕ Operações com Conjuntos em Java

Versão em **Java** do programa de operações com conjuntos, desenvolvida como **aprofundamento pessoal** do trabalho original em Python.

> 📌 **Projeto principal (Python):** [operacoes-conjuntos](https://github.com/Fabiano-Dtreze/operacoes-conjuntos)

Trabalho acadêmico da disciplina de Matemática para Computação — Fatec Osasco.

---

## 📌 Objetivo

Implementar em Java as principais operações da teoria dos conjuntos **sem usar os métodos nativos das coleções**, aplicando laços e condicionais, e comparar cada resultado com a solução nativa da linguagem.

---

## ⚙️ Operações Implementadas

| Operação | Notação | Implementação manual | Solução nativa (Java) |
|---|---|---|---|
| Pertinência | x ∈ A | `pertence(x, A)` | `A.contains(x)` |
| União | A ∪ B | `uniao(A, B)` | `uniaoNativo(A, B)` |
| Interseção | A ∩ B | `interseccao(A, B)` | `interseccaoNativo(A, B)` |
| Diferença | A − B | `diferenca(A, B)` | `diferencaNativo(A, B)` |
| Diferença Simétrica | A △ B | `diferencaSimetrica(A, B)` | `diferencaSimetricaNativo(A, B)` |
| Inclusão | A ⊆ B | `estaContido(A, B)` | `B.containsAll(A)` |
| Inclusão | A ⊇ B | `contem(A, B)` | `A.containsAll(B)` |
| Cardinalidade | \|A\| | `cardinalidade(A)` | `A.stream().distinct().count()` |

---

## 🧠 Decisões de Projeto

**Por que replicar em Java?**
Como aprofundamento pessoal, para compreender as diferenças entre tipagem dinâmica (Python) e estática (Java), e entre linguagens interpretadas e compiladas.

**Diferenças em relação ao Python:**

| Aspecto | Python | Java |
|---|---|---|
| Tipagem | Dinâmica | Estática |
| Execução | Interpretada | Compilada |
| Comparação de Strings | `==` | `.equals()` |
| Estrutura | Script solto | Classe obrigatória |
| Lista | `resultado = []` | `List<String> r = new ArrayList<>()` |

**Ponto crítico:** em Java, comparar Strings com `==` compara **referências de memória**, não conteúdo. Por isso, todas as comparações usam `.equals()`.

---

## 🚀 Como Executar

### Pré-requisitos
- JDK 17 ou superior

### Passos

```bash
# Clone o repositório
git clone https://github.com/Fabiano-Dtreze/operacoes-conjuntos-java.git

# Entre na pasta
cd operacoes-conjuntos-java

# Compile
javac Conjuntos.java

# Execute
java Conjuntos