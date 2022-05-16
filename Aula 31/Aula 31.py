"""
Desafio - Valide um CPF:
CPF = 168.995.350-09
------------------------
1 * 10 =  10          #      1 * 11 = 11 <-
6 * 9 =   54          #      6 * 10 = 60
8 * 8 =   64          #      8 * 9 = 72
9 * 7 =   63          #      9 * 8 = 72
9 * 6 =   54          #      9 * 7 = 63
5 * 5 =   25          #      5 * 6 = 30
3 * 4 =   12          #      3 * 5 = 15
5 * 3 =   15          #      5 * 4 = 20
0 * 2 =   0           #      0 * 3 = 0
         297          #  ->  0 * 2 = 0
11 - (297 % 11) = 11  #        343
11 > 9 = 0            #   11 - (343 % 11) = 9
Digito 1 = 0          #   Digito 2 = 9


"""

cpf = '16899535009'
novo_cpf = cpf[:-2]
total = 0

reverso = 10
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    # Validação de CPF, realizada utilizando estrutura de repetição para que possa ser verificado o index
    # e reverso para chegar ate o valor do cpf itilizando o  metodo simples de calculo em python.
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')
