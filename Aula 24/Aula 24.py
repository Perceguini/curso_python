"""
Split, Join, Enumerate em Python.
*Split - Dividir uma string #str
* Join - Juntar uma lista #str
*Enumerate - Enumerar Elementos da lista #list.
"""

# string = "Pessimismo leva à fraqueza, otimismo ao poder."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
"""
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)} ')
"""
palavra = ''
contagem = 0
"""
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
        print(f'A palavra que aoareceu mais vezes é {palavra}({contagem}x)')

for valor in lista_2:
    print(valor.strip().capitalize())
"""

string = 'Pessimismo leva a fraqueza, otimismo ao poder.'
lista = string.split(' ')

# string2 = ','.join(lista)
# print(string)
# print(lista)
# print(string2)

# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

lista = ['leticia', 'costa', 'perceguini']
n1, n2, n3 = lista

print(n3)
for indice, nome in enumerate(lista):
    print(indice, nome)

