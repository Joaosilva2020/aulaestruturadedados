palavra = input("Digite uma palavra: ")
pilha = list(palavra)
invertida = ""

while pilha:
    invertida += pilha.pop()

print(invertida)
