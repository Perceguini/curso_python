"""
Função (def) em python - *args **kwargs - Parte 3
"""

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Leticia', sobrenome='Perceguini', idade=20)
