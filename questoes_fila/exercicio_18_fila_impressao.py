fila = []

quantidade = int(input("Quantos documentos deseja imprimir? "))

for i in range(quantidade):
    documento = input(f"Digite o nome do {i + 1}o documento: ")
    fila.append(documento)

print("Ordem de impressao:")

while len(fila) > 0:
    documento = fila.pop(0)
    print("Imprimindo:", documento)
