estoque_json = [
    {"id": 1, "nome": "mouse", "preco": 150},
    {"id": 2, "nome": "teclado", "preco": 180},
    {"id": 3, "nome": "fone", "preco": 70}
]

new_name = input("Digite o nome do novo produto: ")

new_preco = int(input("Digite o preço: "))

new_produto = {
    "id": len(estoque_json) + 1,
    "nome": new_name,
    "preco": new_preco
}

estoque_json.append(new_produto)

print("\nEstoque atualizado:")




print(new_produto["nome"])