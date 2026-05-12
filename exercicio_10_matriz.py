matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

soma = 0
diagonal_principal = []

print("Todos os valores:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j])
        soma += matriz[i][j]

for i in range(3):
    diagonal_principal.append(matriz[i][i])

print("Soma de todos os elementos:", soma)
print("Diagonal principal:", diagonal_principal)
