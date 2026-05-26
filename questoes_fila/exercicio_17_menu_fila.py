fila = []
opcao = ""

while opcao != "5":
    print("1 - Enfileirar")
    print("2 - Desenfileirar")
    print("3 - Mostrar primeiro")
    print("4 - Mostrar fila")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        valor = input("Digite um valor: ")
        fila.append(valor)
        print("Valor adicionado.")
    elif opcao == "2":
        if len(fila) > 0:
            removido = fila.pop(0)
            print("Removido:", removido)
        else:
            print("Fila vazia.")
    elif opcao == "3":
        if len(fila) > 0:
            print("Primeiro:", fila[0])
        else:
            print("Fila vazia.")
    elif opcao == "4":
        print("Fila:", fila)
    elif opcao == "5":
        print("Saindo...")
    else:
        print("Opcao invalida.")
