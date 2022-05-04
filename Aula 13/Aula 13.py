"""
Len - Quantidade de caracteres
"""
usuario = input('Digite o seu usuario:  ')
qtd_caracteres  = len(usuario)

print(usuario, qtd_caracteres, type (qtd_caracteres))

if qtd_caracteres < 6:
    print('Necessario digitar pelo menos 6 catacteres')

else:
    print('Você foi cadastrado no sistema')

string1 = input('Digite algo:'  )
string12 = input('Digiete algo mais:' )

print(f'A quantidade de racacteries digitadas foi {len (string1) + len(string12)}')