fila = []

for i in range(5):
    nome = input(f"Digite o {i + 1}o nome: ")
    fila.append(nome)

print("Nomes removidos na ordem em que foram digitados:")

while len(fila) > 0:
    nome = fila.pop(0)
    print(nome)
