""""
Condições IF, ELIF, e ELSE - Aula 4
"""

if True:
    print("verdadeiro.")

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)

if False:
    print('verdadeiro')
elif False:
    print("Agora é verdadeiro")
elif True:
    print("Agora é verdadeiro")
    nome = input("Qual o seu nome?")

    print(f'Seu nome é {nome}')
elif False:
    print('Mais uma verdadeira')
    print(22 + 22)
else:
    print("não e verdadeiro")
    print(olá)
