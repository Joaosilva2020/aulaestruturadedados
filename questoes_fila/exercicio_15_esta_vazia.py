def esta_vazia(fila):
    if len(fila) == 0:
        return True
    else:
        return False


fila = []

print("A fila esta vazia?", esta_vazia(fila))

fila.append("Ana")

print("A fila esta vazia?", esta_vazia(fila))
