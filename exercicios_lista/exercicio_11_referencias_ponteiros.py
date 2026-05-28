"""
=============================================================================
RESPOSTAS TEORICAS
=============================================================================
QUESTAO 1: O que e um ponteiro em programacao?
Resposta: Um ponteiro e uma variavel cujo valor e o endereco de memoria de
outra variavel. Em vez de guardar um dado (como o numero 10), ele guarda o local
fisico na memoria RAM onde esse dado esta armazenado.

QUESTAO 2: Em C, o que significa armazenar o endereco de memoria de outra variavel?
Resposta: Significa que a variavel (ponteiro) aponta diretamente para o local
fisico no hardware onde a outra variavel esta. Se voce altera o valor no endereco
apontado, a variavel original e modificada automaticamente, pois ambas compartilham
o mesmo espaco na RAM.

QUESTAO 3: Python possui ponteiros como C? Como Python trabalha com referencias?
Resposta: Python nao possui ponteiros explicitos (voce nao manipula enderecos
de memoria diretamente como em C). Em vez disso, Python usa "Referencias". Tudo
em Python e um Objeto. Variaveis sao apenas "etiquetas" (nomes) que colamos nesses
objetos na memoria.

QUESTAO 5: O valor de referencia tambem muda ao alterar "numero"?
Resposta: Nao. Numeros inteiros sao tipos IMUTAVEIS em Python. Quando alteramos
"numero", o Python cria um novo objeto na memoria com o novo valor e move a etiqueta
"numero" para ele. A variavel "referencia" continua apontando para o objeto antigo.

QUESTAO 7: Por que, no caso de listas, duas variaveis apontam para o mesmo objeto?
Resposta: Porque listas sao tipos MUTAVEIS. Ao fazer "lista2 = lista1", o Python
nao cria uma copia dos dados, ele apenas cola uma segunda etiqueta no mesmo
objeto na memoria. Alterar a lista por qualquer uma das variaveis afetara o objeto
unico que ambas referenciam.

QUESTAO 10: Qual a diferenca entre usar == e is em Python?
Resposta: O operador "==" compara os VALORES (se o conteudo e igual). O operador
"is" compara a IDENTIDADE (se ambas as variaveis apontam exatamente para o mesmo
endereco de memoria / mesmo objeto).

QUESTAO 14: Por que objetos mutaveis (listas/dicionarios) podem ser alterados em funcoes?
Resposta: Porque a funcao recebe a referencia (o endereco) do objeto original.
Como o objeto e mutavel, a funcao consegue alterar o conteudo daquele endereco,
refletindo a mudanca fora da funcao.

QUESTAO 15: Por que objetos imutaveis (inteiros/strings) nao sao alterados em funcoes?
Resposta: Porque nao e possivel alterar o valor de um objeto imutavel na memoria.
Qualquer tentativa de alteracao dentro da funcao faz o Python criar um novo objeto
localmente, nao afetando a variavel original que ficou fora da funcao.

QUESTAO 19: Diferenca entre Copia Rasa (Shallow) e Copia Profunda (Deep Copy).
Resposta: A copia rasa (copy) cria um novo objeto principal, mas se houver objetos
mutaveis dentro dele (como uma lista dentro de outra lista), as referencias internas
sao mantidas. A copia profunda (deepcopy) cria um clone completo de absolutamente
tudo, garantindo independencia total.
=============================================================================
"""

import copy

print("=== EXECUTANDO EXERCICIOS DE REFERENCIAS (ADS - UNIC) ===\n")

# =============================================================================
# QUESTAO 4: Crie numero e referencia. Exiba ambas.
# =============================================================================
print("--- Questao 4 ---")
numero = 10
referencia = numero
print(f"Numero: {numero} | Referencia: {referencia}\n")


# =============================================================================
# QUESTAO 5: Altere o numero. A referencia muda? (Demonstracao pratica)
# =============================================================================
print("--- Questao 5 ---")
numero = 20
print("Alteramos 'numero' para 20.")
print(f"Numero agora e: {numero} | Referencia continua: {referencia}")
print("Explicacao: Inteiros sao imutaveis!\n")


# =============================================================================
# QUESTAO 6: Listas, ponteiros e mutabilidade.
# =============================================================================
print("--- Questao 6 ---")
valores = [10, 20, 30]
ponteiro_lista = valores
ponteiro_lista[0] = 999

print(f"Lista 'valores' original apos alteracao via ponteiro: {valores}")
print("Explicacao: Listas sao mutaveis, ambas as variaveis apontam para o mesmo local.\n")


# =============================================================================
# QUESTAO 8: Use a funcao id() para mostrar o endereco de memoria.
# =============================================================================
print("--- Questao 8 ---")
print(f"Endereco de memoria de 'valores':        {id(valores)}")
print(f"Endereco de memoria de 'ponteiro_lista': {id(ponteiro_lista)}")
print("Os IDs sao identicos, provando que e o mesmo objeto na memoria.\n")


# =============================================================================
# QUESTAO 9: Listas iguais, mas objetos diferentes.
# =============================================================================
print("--- Questao 9 ---")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(f"ID da lista 1: {id(lista1)}")
print(f"ID da lista 2: {id(lista2)}")
print("Apesar de terem os mesmos numeros, sao objetos distintos na memoria!\n")


# =============================================================================
# QUESTAO 11: Programa comparando == e is.
# =============================================================================
print("--- Questao 11 ---")
a = [5, 6, 7]
b = [5, 6, 7]
c = a

print(f"a == b (Valores sao iguais?): {a == b}")
print(f"a is b (Sao o mesmo objeto?): {a is b}")
print(f"a is c (Sao o mesmo objeto?): {a is c}\n")


# =============================================================================
# QUESTAO 12: Funcao que altera lista (Passagem por referencia mutavel).
# =============================================================================
print("--- Questao 12 ---")


def alterar_lista(lista):
    lista.append("NOVO")


minha_lista = ["A", "B", "C"]
print(f"Lista antes da funcao: {minha_lista}")
alterar_lista(minha_lista)
print(f"Lista depois da funcao: {minha_lista}\n")


# =============================================================================
# QUESTAO 13: Funcao que tenta alterar inteiro (Imutavel).
# =============================================================================
print("--- Questao 13 ---")


def alterar_numero(num):
    num = 100


meu_numero = 50
print(f"Numero antes da funcao: {meu_numero}")
alterar_numero(meu_numero)
print(f"Numero depois da funcao: {meu_numero} (Nao mudou!)\n")


# =============================================================================
# QUESTAO 16: Dicionarios e referencias.
# =============================================================================
print("--- Questao 16 ---")
aluno = {"nome": "Carlos", "idade": 25}
referencia_aluno = aluno

referencia_aluno["idade"] = 30
print(f"Dicionario original 'aluno': {aluno}\n")


# =============================================================================
# QUESTAO 17: Usando o copy() para listas.
# =============================================================================
print("--- Questao 17 ---")
lista_base = [1, 2, 3]
lista_copiada = lista_base.copy()

lista_copiada.append(4)
print(f"Lista Base Original: {lista_base}")
print(f"Lista Copiada:       {lista_copiada}\n")


# =============================================================================
# QUESTAO 18: O problema da copia rasa (Listas aninhadas).
# =============================================================================
print("--- Questao 18 (Copia Rasa) ---")
lista_externa = [[1, 2], 3, 4]
copia_rasa = lista_externa.copy()

copia_rasa[0][0] = 99
print(f"Lista Externa Original foi afetada: {lista_externa}")
print("Isso ocorreu porque .copy() nao copia os objetos internos profundos.\n")


# =============================================================================
# QUESTAO 19: Exemplo de Shallow Copy vs Deep Copy.
# =============================================================================
print("--- Questao 19 ---")
original = [[1, 2], 3]

# Copia Rasa (Shallow)
rasa = copy.copy(original)
rasa[0][0] = "MODIFICADO RASA"

# Copia Profunda (Deep)
profunda = copy.deepcopy(original)
profunda[0][0] = "MODIFICADO DEEP"

print(f"Lista Original (afetada pela rasa): {original}")
print(f"Copia Profunda (totalmente isolada): {profunda}\n")


# =============================================================================
# QUESTAO 20: Simulando ponteiros de C em Python com Listas.
# =============================================================================
print("--- Questao 20 (Simulador de Ponteiro) ---")
# Para simular um ponteiro que aponta para um valor solto, colocamos o valor
# dentro de uma lista (que e mutavel e seu endereco de memoria sera compartilhado).
variavel_simulada = [42]
ponteiro = variavel_simulada

print(f"Valor inicial lido pelo ponteiro: {ponteiro[0]}")

# O ponteiro modifica o dado no endereco de memoria compartilhado.
ponteiro[0] = 100

print(f"Variavel original apos o ponteiro alterar a memoria: {variavel_simulada[0]}")
print("=== FIM DA EXECUCAO DAS LISTAS DA DISCIPLINA ===")
