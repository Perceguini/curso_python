"""
Lista em python
*Fatiamento
*Append, insert, pop, del, clear, extend, min, max.
*Range

booleanos = True
inteiros = 10
flutuante = -10.10
strings = 'Textos'
"""
#         0    1    2    3    4    5
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#    -    5    4    3    2    1
# print(lista[::-1])


# l2 = list(range(0, 100, 8))
# print(l2)

# l2 = ['String', True, 10, -20.5]

# for elem in l2:
# print(f'O tipo de {elem} é {type(elem)} e seu valor é {elem}')

secreto = 'dinossauro'
digitadas = []

while True:
    letra = input('Digite uma letra:  ')

    if len(letra) > 1:
        print('Ahhhhhhhhh isso não vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHHUUUUULLLLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFZZZ:  a letra "{letra}" NÃO EXISTE NA PALAAVRA SECRETA. ')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += '*'

    if len(secreto) == len(digitadas):
        print(f'UHuuuullll, parabéns vc acertou seu {secreto}')
        break
    else:
        print(secreto_temporario)

