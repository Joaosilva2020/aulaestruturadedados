pilha = []

for i in range(5):
    nome = input(f"Digite o {i + 1}o nome: ")
    pilha.append(nome)

while pilha:
    print(pilha.pop())
