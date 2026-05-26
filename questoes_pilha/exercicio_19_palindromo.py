palavra = input("Digite uma palavra: ")
pilha = list(palavra)
invertida = ""

while pilha:
    invertida += pilha.pop()

if palavra == invertida:
    print("E palindromo")
else:
    print("Nao e palindromo")
