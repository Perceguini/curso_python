"""
Operadores Lógicos - Aula 4
and, or, not
in e not in

(Verdadeiro e Falso) = Falso
comparacao1 and comparacao2

Verdadeiro ou verdadeiro
comp1
OR
comp2

a = 2
b = 3

if not b > a:
    print('B é maior do que A')

else:
    print('A é maior do que B')

a = '32'
b = 1

if not b:
    print('Por favor preencha o valor de B')

nome = 'Leticia'

if 'o' in nome:
    print('existe')
else:
    print('Não existe')

nome = 'Perceguini'

if 'Per' not in nome:
    print('execultei')
else:
    print('Existe o texto')
"""
usuario = input('Nome de usuário:  ')
senha = input('senha do usuário:  ')

usuario_bd = 'leticia '
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('você está logado no sistema')

else:
    print('Usuário ou senha inválida')
