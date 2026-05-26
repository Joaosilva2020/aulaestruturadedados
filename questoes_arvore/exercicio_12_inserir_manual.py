class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(20)

print("Raiz:", raiz.valor)
