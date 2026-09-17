valor_total = 10.0
saldo_usuario = 9.0
cupom_valido = False
cpm= input("Voce Possui Cupom? s/n: ")

if cpm == "s":
    cupom_valido = True
else:
    cupom_valido = False


if cupom_valido == True:
    valor_total = valor_total  * 0.9
     #valor_total *= 0.9


if saldo_usuario >= valor_total:
    print("Pedido Criado!")

elif saldo_usuario < valor_total:
    print("Saldo insuficiente!")




