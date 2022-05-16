"""
Desafio de contadores:
for / while
0  10
1  9
2  8
3  7
4  6
5  5
6  4
7  3
8  2
"""
contador = 0
contador2 = 10

while contador < 10:
    print(f'1° - {contador} | {contador2}')

    contador += 1
    contador2 -= 1

contador = 0
print("\n###################################\n")
while contador < 10:
    print(f'2° - {contador} | {10 - contador}')

    contador += 1
