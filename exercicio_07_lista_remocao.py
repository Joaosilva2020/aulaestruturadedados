frutas = ["banana", "maca", "laranja", "uva", "manga"]

print("Frutas:", frutas)
fruta = input("Digite a fruta que deseja remover: ").lower()

if fruta in frutas:
    frutas.remove(fruta)
    print("Fruta removida com sucesso.")
else:
    print("Fruta nao encontrada.")

print("Lista atualizada:", frutas)
