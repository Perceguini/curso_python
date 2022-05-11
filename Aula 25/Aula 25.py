"""
Enumerate - Enumerar elementos da lista # list

Simplesmente enumera uma lista.
"""

lista = [
    #    0         1            2
    ['Leticia', 'Costa', 'Perceguini'],  # 0
    ['Kairo', 'Vinicius', 'Losano'],  # 1
    ['Maria', 'Joana', 'Claudia'],  # 2
]

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)


# print(lista[1][2])

# enumerada = list(enumerate(lista))
# print(enumerada[1][1][2])

"""
[ <----- Enumereite
  0  1
 (0, ['Leticia', 'Costa', 'Perceguini']), #0
 (1, ['Kairo', 'Vinicius', 'Losano']),  #1
 (2, ['Maria', 'Joana', 'Claudia'])     #2 
 ]
"""
