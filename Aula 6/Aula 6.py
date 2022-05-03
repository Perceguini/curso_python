"""
Iniciar com letra, pode conter numeros, separar _, letras minúsculas
"""
# nome = input("Qual o seu nome? ")
# idade = int(input("Qual a sua idade? "))  # int
# altura = float(input("Qual a sua altura? "))  # float
nome = 'Leticia'
idade = 20  # int
altura = 1.65  # float
e_maior = idade > 18  # bool
peso = 6.7  # float
# peso = float(input("Qual o seu peso (KG)? "))
imc = peso / (altura ** 2)

print('nome:', nome)
print('idade:', idade)
print('altura:', altura)
print('nome:', nome)
print(f'e maior: {e_maior}')
print(f'peso: {peso}')
print(idade * altura)

"""
Ex:
"""
print(nome, 'tem', 'idade, anos de idade e seu imc', imc)
