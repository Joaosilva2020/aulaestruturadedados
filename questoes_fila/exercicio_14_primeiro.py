def primeiro(fila):
    if len(fila) > 0:
        return fila[0]
    else:
        return "Fila vazia"


fila = ["Ana", "Bruno", "Carlos"]

print("Primeiro da fila:", primeiro(fila))
print("Fila:", fila)
