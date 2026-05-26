fila = []
senha = 1
opcao = ""

while opcao != "3":
    print("1 - Gerar senha")
    print("2 - Chamar senha")
    print("3 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        fila.append(senha)
        print("Senha gerada:", senha)
        senha += 1
    elif opcao == "2":
        if len(fila) > 0:
            chamada = fila.pop(0)
            print("Senha chamada:", chamada)
        else:
            print("Nenhuma senha na fila.")
    elif opcao == "3":
        print("Saindo...")
    else:
        print("Opcao invalida.")

    print("Fila de senhas:", fila)
