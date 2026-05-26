pilha = []

while True:
    print("1-Empilhar 2-Desempilhar 3-Topo 4-Mostrar pilha 5-Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
        pilha.append(input("Valor: "))
    elif opcao == "2":
        print(pilha.pop() if pilha else "Pilha vazia")
    elif opcao == "3":
        print(pilha[-1] if pilha else "Pilha vazia")
    elif opcao == "4":
        print(pilha)
    elif opcao == "5":
        break
