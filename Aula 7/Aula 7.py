nome = 'Leticia'
idade = 20  # int
altura = 1.65  # float
e_maior = idade > 18  # bool
peso = 6.7  # float
imc = peso / (altura ** 2)

print(nome, 'tem', 'idade, anos de idade e seu imc', imc)
print(f'{nome} tem{idade} idade, anos de idade e seu imc {imc:.2f}')
print('{} tem {} anos de idade e seu imc {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc {im}'.format(n=nome, i=idade, im=imc))

