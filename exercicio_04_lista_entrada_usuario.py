numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}o numero: "))
    numeros.append(numero)

print("Lista:", numeros)
print("Soma dos valores:", sum(numeros))
