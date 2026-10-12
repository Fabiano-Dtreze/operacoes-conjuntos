# ============================================================
# OPERAÇÕES MANUAIS (sem usar operadores prontos de set)
# ============================================================

def pertence(x, A):
    """Verifica se x pertence a A (sem usar 'in')."""
    for elemento in A:
        if elemento == x:
            return True
    return False


def uniao(A, B):
    """União: elementos de A ou de B, sem repetição."""
    resultado = []
    for x in A:
        if not pertence(x, resultado):
            resultado.append(x)
    for x in B:
        if not pertence(x, resultado):
            resultado.append(x)
    return resultado


def interseccao(A, B):
    """Interseção: elementos que estão em A e em B."""
    resultado = []
    for x in A:
        if pertence(x, B) and not pertence(x, resultado):
            resultado.append(x)
    return resultado


def diferenca(A, B):
    """A - B: elementos de A que não estão em B."""
    resultado = []
    for x in A:
        if not pertence(x, B) and not pertence(x, resultado):
            resultado.append(x)
    return resultado


def diferenca_simetrica(A, B):
    """(A - B) ∪ (B - A)."""
    ab = diferenca(A, B)
    ba = diferenca(B, A)
    return uniao(ab, ba)


def contem(A, B):
    """A contém B? (todo elemento de B está em A)."""
    for x in B:
        if not pertence(x, A):
            return False
    return True


def esta_contido(A, B):
    """A está contido em B?"""
    return contem(B, A)


def cardinalidade(A):
    """Conta elementos únicos de A sem usar len(set(A))."""
    contador = 0
    vistos = []
    for x in A:
        if not pertence(x, vistos):
            vistos.append(x)
            contador += 1
    return contador


def complemento(A, U):
    """Complemento de A em relação a U: U - A."""
    return diferenca(U, A)


# ============================================================
# LEITURA E MENU
# ============================================================

def ler_conjunto(nome):
    entrada = input(f"Digite os elementos de {nome} separados por espaço (Enter para vazio): ")
    if entrada.strip() == "":
        return []
    return entrada.split()


def mostrar_resultado(titulo, manual, nativo):
    print(f"\n--- {titulo} ---")
    print(f"  Implementação manual: {manual}")
    print(f"  Solução nativa (set): {nativo}")
    print(f"  Iguais? {'✅ SIM' if sorted(map(str, manual)) == sorted(map(str, nativo)) else '❌ NÃO'}")


def menu():
    A = ler_conjunto("A")
    B = ler_conjunto("B")

    setA = set(A)
    setB = set(B)

    while True:
        print("\n================ MENU ================")
        print("1 - União (A ∪ B)")
        print("2 - Interseção (A ∩ B)")
        print("3 - Diferença (A - B)")
        print("4 - Diferença (B - A)")
        print("5 - Diferença Simétrica (A △ B)")
        print("6 - Pertinência (x ∈ A?)")
        print("7 - Inclusão (A contém B? / A ⊂ B?)")
        print("8 - Cardinalidade de A e B")
        print("9 - Complemento de A em relação a U")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            mostrar_resultado("União", uniao(A, B), setA | setB)
        elif opcao == "2":
            mostrar_resultado("Interseção", interseccao(A, B), setA & setB)
        elif opcao == "3":
            mostrar_resultado("A - B", diferenca(A, B), setA - setB)
        elif opcao == "4":
            mostrar_resultado("B - A", diferenca(B, A), setB - setA)
        elif opcao == "5":
            mostrar_resultado("Diferença Simétrica", diferenca_simetrica(A, B), setA ^ setB)
        elif opcao == "6":
            x = input("Elemento a verificar: ").strip()
            m = pertence(x, A)
            n = x in setA
            print(f"\n  Manual: {m} | Nativo: {n} | Iguais? {'✅' if m == n else '❌'}")
        elif opcao == "7":
            m1 = contem(A, B); n1 = setB.issubset(setA)
            m2 = esta_contido(A, B); n2 = setA.issubset(setB)
            print(f"\n  A contém B?  Manual: {m1} | Nativo: {n1} | {'✅' if m1 == n1 else '❌'}")
            print(f"  A ⊂ B?       Manual: {m2} | Nativo: {n2} | {'✅' if m2 == n2 else '❌'}")
        elif opcao == "8":
            cm, cn = cardinalidade(A), len(setA)
            dm, dn = cardinalidade(B), len(setB)
            print(f"\n  |A| Manual: {cm} | Nativo: {cn} | {'✅' if cm == cn else '❌'}")
            print(f"  |B| Manual: {dm} | Nativo: {dn} | {'✅' if dm == dn else '❌'}")
        elif opcao == "9":
            U = ler_conjunto("Universo U")
            mostrar_resultado("Complemento de A em U", complemento(A, U), set(U) - setA)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()