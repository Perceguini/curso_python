from random import choice

"""
Operador ternário em python
"""
"""
logged_user = False

if logged_user == True:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

logged_user = False

mgs = 'Usuário logado.' if (logged_user == True) else 'Usuário precisa logar'
print(mgs)
"""
idade = input('Qual a sua idade?  ')

if not idade.isnumeric():
    print(choice(['Você precisa digitaar apenas números.', "Hahaha bobão"]))
else:
    e_de_maior = (int(idade) >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    print(msg)
