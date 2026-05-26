def desenfileirar(fila):
    if len(fila) > 0:
        return fila.pop(0)
    else:
        return "Fila vazia"


fila = ["Ana", "Bruno", "Carlos"]

removido = desenfileirar(fila)

print("Removido:", removido)
print("Fila:", fila)
