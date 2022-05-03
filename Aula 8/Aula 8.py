"""
Criar variaveis para nomes (str), idade (int),
Altura (float) e peso (float) de uma pessoa
Criar variavel com o ano atual (int),
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter IMC da pessoa com 2 casa decimais (pesso e na altua da pessoa)
Exibir um taxo com todos os valores na tala usando F-strings (com as chaves)
"""
nome = 'Leticia'
idade = 20  # int
altura = 1.65  # float
e_maior = idade > 18  # bool
peso = 6.7  # float
imc = peso / (altura ** 2)
ano = 2022 - idade

"""print(nome, 'tem', idade, 'anos de idade e a sua altura é', altura)"""
print('{} tem {} anos de idade e a sua altura é {}'.format(nome, idade, altura))
"""print(nome, 'tem', altura, 'altura e o seu peso é', peso)"""
print('{} tem {} altura e o seu peso é {}'.format(nome, altura, peso))
print('Ano 2022')
print(2022 - idade)
print(f"{peso / (altura ** 2):.2f} kairo foda")
