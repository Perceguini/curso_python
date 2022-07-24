from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
# print('O computador escolheu {}'.format(itens[computador]))
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(0.5)
print('*-' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('*-' * 12)

if computador == 0:  # Computador jogou pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:  # Computador jogou papel
        print('JOGADOR VENCE!')

    elif jogador == 2:
        print('COMPUTADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVALIDA')
