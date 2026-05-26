fila = []
opcao = ""

while opcao != "3":
    print("1 - Adicionar pessoa")
    print("2 - Atender pessoa")
    print("3 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Digite o nome da pessoa: ")
        fila.append(nome)
        print("Pessoa adicionada.")
    elif opcao == "2":
        if len(fila) > 0:
            pessoa = fila.pop(0)
            print("Atendendo:", pessoa)
        else:
            print("Fila vazia.")
    elif opcao == "3":
        print("Saindo...")
    else:
        print("Opcao invalida.")

    print("Fila:", fila)
