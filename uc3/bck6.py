autentich_user = [
     {"id": 101, "nome": "Alice", "autenticado": True},
       {"id": 102, "nome": "Bruno", "autenticado": True}, 
       {"id": 103, "nome": "Carla", "autenticado": True} ]

verificaçao = int(input("Digite Seu Id: "))

encontrado = False

for user in autentich_user:
    if user ["id"] == verificaçao and user ["autenticado"] == True:
        print(f"Hi {user["nome"]}!")
        encontrado = True
        break


if encontrado == False:
    print("User Nao Encontrado!")