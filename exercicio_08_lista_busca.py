numeros = [5, 12, 8, 20, 33, 7, 15, 40, 2, 18]

numero_busca = int(input("Digite um numero para buscar: "))

if numero_busca in numeros:
    posicao = numeros.index(numero_busca)
    print("O numero esta na lista.")
    print("Posicao:", posicao)
else:
    print("O numero nao esta na lista.")
