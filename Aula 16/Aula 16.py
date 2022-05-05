"""
Faça um progama que peça para os usuário digitar um número inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é número inteiro.
"""

numero = input("Digite um número: ")

if numero.isdigit():
    if (int(numero) % 2) == 0:
        print("\033[94mSeu número é par\033[0m")
    else:
        print("\033[92mSeu número é impar\033[0m")
else:
    print("\033[93mNão é um numero inteiro, digite números inteiros!\033[0m")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saldação apropriada. ex
Bom dia 0-11, Boa tarde 12-17 e Boa noite18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tives 4 letras ou
menos escreva "seu nome é curto"; Se tiver emtre 5 ou 6 letras escreva "Seu nome é normal";
Maior que 6 escreva "Seu nome é muito longo".
"""
# usuario = input('Digite o seu  nome:  ')
