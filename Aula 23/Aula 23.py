"""
For / Else em Python
"""

variavel = ['Leticia', 'Costa', 'Perceguini']
"""
for valor in variavel:
    print(valor)
    continue (Para cintinuar o laço)
    break  (Termina o laço e não continua mais.)

for valor in variavel:
    print(valor)
    break
    print(valor)

for valor in variavel:
    if valor.startswith('L'):
        print('Começa com L', valor)
    else:
        print('Não começa com L', valor)
"""
for valor in variavel:
    if valor.lower().startswith('l'):
        continue
    print(valor)
