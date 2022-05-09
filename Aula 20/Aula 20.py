"""
While / Else - Aula 8
Contadores
Acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    contador += 1

    acumulador = acumulador + contador
    contador += 1

    if contador > 5:
        break

else:
    print('Cheguei no else.')
