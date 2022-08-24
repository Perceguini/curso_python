from itertools import count

"""
Zip - Unindo iteráveis
Zip_longuest - Itertools
"""
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Mente Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades
)
for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
