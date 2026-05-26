pratos = []

while True:
    opcao = input("1-Adicionar prato 2-Remover prato 3-Sair: ")

    if opcao == "1":
        prato = input("Nome do prato: ")
        pratos.append(prato)
    elif opcao == "2":
        if pratos:
            print("Removido:", pratos.pop())
        else:
            print("Pilha vazia")
    elif opcao == "3":
        break
