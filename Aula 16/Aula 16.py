"""
Faça um progama que peça para os usuário digitar um número inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é número inteiro.
"""

# numero = input("Digite um número: ")

# if numero.isdigit():
#    if (int(numero) % 2) == 0:
#        print("\033[94mSeu número é par\033[0m")
#   else:
#        print("\033[92mSeu número é impar\033[0m")
# else:
# print("\033[93mNão é um numero inteiro, digite números inteiros!\033[0m")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saldação apropriada. ex
Bom dia 0-11, Boa tarde 12-17 e Boa noite18-23.
"""
horario = input("Digite a hora (0-23): ")

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print("Horario deve estar entre 0-23")
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Bao tarde')
        else:
            print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tives 4 letras ou
menos escreva "seu nome é curto"; Se tiver entre 5 ou 6 letras escreva "Seu nome é normal";
Maior que 6 escreva "Seu nome é muito longo".
"""
nome = input('Digite o primeiro nome de usuário:  ')
qtd_caracteres = len(nome)

print(nome, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres <= 4:
    print('Seu nome é curto.')

elif qtd_caracteres <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito longo')
