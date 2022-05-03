"""
Iniciar com letra, pode conter numeros, separar _, letras minúsculas
"""
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))  # int
altura = float(input("Qual a sua altura? "))  # float
e_maior = idade > 18  # bool
peso = float(input("Qual o seu peso (KG)? "))
imc = peso / (altura ** 2)

print('nome:', nome)
print('idade:', idade)
print('altura:', altura)
print('nome:', nome)
print('e maior:', e_maior)
print('peso:', peso)
print(idade * altura)

"""
Ex:
"""
