"""
Operadores Relacionais - Aula 4
==Igualdade >Maior que
>=Maior que ou igual a
<Menor que
<=Menor que ou igual a
!=Diferente
Funciona com numeros e letras
print(2 == 2)
print(2 > 2)
print(2 >= 2)
print(2 < 2)
print(2 <= 2)

num_1 = 2  # int
num_2 = 2  # string
print(num_1 == num_2)

expressao = (num_1 == num_2)
print(expressao)

expressao = (num_1 > num_2)
print(expressao)

expressao = (num_1 >= num_2)
print(expressao)

expressao = (num_1 < num_2)
print(expressao)

expressao = (num_1 >= num_2)
print(expressao)

expressao = (num_1 != num_2)
print(expressao)
"""
nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')

idade = int(idade)

# Limite para pegar empréstimo
idade_menor = 20  # Jovem
idade_maior = 30  # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
