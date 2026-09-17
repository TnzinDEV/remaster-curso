import random
TabY=["A","B","C","D","E"]
TabX=["1","2","3","4","5"]

tabuleiro= [["."] * 5 for _ in range(5)]

a = "~"
b = "-"
n ="X"



item1=random.choice(TabY)
item2=random.choice(TabX)

number=item1+item2
print(number)

ln = TabY.index(item1)
cn = int(item2) -1

for TabY in TabX:
    print(f"{TabY}")

for linha in tabuleiro:
    print(" ".join(linha))

tabuleiro [ln][cn] = "N"



while True:
    x= int(input("Digite a Coluna Horizontal: ")) -1
    y= int(input("Digite a Coluna Vertical: ")) -1

    if tabuleiro [x][y] == "N":
        print("Acertou Mizeravel!")
        tabuleiro [x][y] = "X"
        print(" ".join(linha))
        break
    else:
        print("Errou Burrao kkj!")
        tabuleiro [x][y] = "O"


    for linha in tabuleiro:
        linha_visual = []

        for posicao in linha:
            if posicao == "N":
                linha_visual.append(".")
            else:
                linha_visual.append(posicao)
    
        print(" ".join(linha_visual))