"""
Funções (def) em python - return
"""


def divisao(n1, n2):
    if n2 == 0:
        return
    return n2 / n1


divide = divisao(8, 4)  #Divide: none

if divide:
    print(divide)
else:
    print('Conta invalida.')
