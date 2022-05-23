"""
Função Def em python (parte 1)
"""


# def usado para criar qualquer função
def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replece('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()
print(variavel)
