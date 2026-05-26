class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def contar_nos(no):
    if no is None:
        return 0
    return 1 + contar_nos(no.esquerda) + contar_nos(no.direita)


raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(20)

print("Quantidade de nos:", contar_nos(raiz))
