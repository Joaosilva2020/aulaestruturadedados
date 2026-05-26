fila_caixa = []

print("Uma situacao real de fila e a fila de um caixa de mercado.")
print("A primeira pessoa que entra na fila deve ser a primeira atendida.")

fila_caixa.append("Ana")
fila_caixa.append("Bruno")
fila_caixa.append("Carlos")

print("Fila do caixa:", fila_caixa)

while len(fila_caixa) > 0:
    cliente = fila_caixa.pop(0)
    print("Atendendo cliente:", cliente)

print("Todos os clientes foram atendidos.")
