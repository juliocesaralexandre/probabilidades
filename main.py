import itertools

def gerar_combinacoes(qtd_jogos):
    opcoes = ["V", "E", "P"]  # vitoria, Empatar, Perder
    return list(itertools.product(opcoes, repeat=qtd_jogos))

def main():
    print("=== Gerador de Combinações ===")
    qtd = int(input("Quantos jogos você quer? "))

    combinacoes = gerar_combinacoes(qtd)
    total = len(combinacoes)

    print(f"\nTotal de combinações possíveis: {total}\n")
    print("Pressione ENTER para começar a validar.\n")
    input()

    for i, comb in enumerate(combinacoes, start=1):
        linha = " - ".join(comb)
        print(f"Combinação {i}/{total}: {linha}")

        ok = input("Digite OK para validar: ").strip().lower()
        while ok != "ok":
            ok = input("Digite OK para validar: ").strip().lower()

        print("✔ Validada!\n")

    print("Todas as combinações foram validadas!")

if __name__ == "__main__":
    main()

