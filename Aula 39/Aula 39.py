"""
1- Crie uma funcao1 que recebe uma funcao2 como parâmetro  e retorne o valor da funcao2 executada.
"""


def ola():
    return 'Ola'


def mestre(funcao):
    return funcao()


executando = mestre(ola)
print(executando)

"""
2- Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor da funcao2 executada. faça
a funcao1 executar das duas funções que recebem um número diferente de argumentos.
"""


# args e kwargs é usado como parametro para função interna.
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'


executando = mestre(oi, 'Leticia')
executando2 = mestre(saudacao, 'Leticia', saudacao='Bom dia')
print(executando)
print(executando2)
