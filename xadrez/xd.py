
tabuleiro = [["□" for _ in range(8)] for _ in range(8)]



def mostrar_tabuleiro(tabuleiro):

    print("\n    A   B   C   D   E   F   G   H")
    print("  +---+---+---+---+---+---+---+---+")

    for i, linha in enumerate(tabuleiro):

        print(f"{8 - i} | " + " | ".join(linha) + f" | {8 - i}")
        print("  +---+---+---+---+---+---+---+---+")

    print("    A   B   C   D   E   F   G   H")







brancas = "Brancas"
pretas = "Pretas"

jogador1 = brancas
jogador2 = pretas

REI_branca = "Rb"
RAINHA_branca = "Qb"
TORRE_branca = "Tb"
BISPO_branca = "Bb"
CAVALO_branca = "Cb"
PEAO_branca = "Pb"



REI_preta = "Rp"
RAINHA_preta = "Qp"
TORRE_preta = "Tp"
BISPO_preta = "Bp"
CAVALO_preta = "Cp"
PEAO_preta = "Pp"


mostrar_tabuleiro(tabuleiro)