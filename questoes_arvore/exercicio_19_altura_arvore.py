class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no.esquerda), altura(no.direita))


raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(20)
raiz.esquerda.esquerda = No(3)

print("Altura:", altura(raiz))
