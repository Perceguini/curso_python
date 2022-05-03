"""
Entrada de dados - Aula 3
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos.  '
      f'{nome} nasceu em {ano_nascimento}.')

numero_1 = int(input('digite um numero:'))
numero_2 = int(input('digite outro numero:'))

print(numero_1 + numero_2)