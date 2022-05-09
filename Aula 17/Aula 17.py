"""
Formatando valores com modificadores - Aula 5
:s Texto (strings)
:d Inteiros (int)
:f Números de pontos flutuante (float)
:. (NÚMERO) f - Quantidade de casas descimais (float) :.2f
: (CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')


# nome = 'leticia'
# print(f'{nome:s}')


num_1 = 1
print(f'{num_1:0>10}')
num_2 = 150
print(f'{num_2:0^10.2f}')

nome = 'leticia'
print(f'{nome:#^50}')

nome = 'leticia perceguini'
nome_formatado = '{:@>15}'.format(nome)

print(nome_formatado)
