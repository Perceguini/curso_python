"""
1 - Crie uma função que exibe uma saldacao com os primeiros parârameros e nome.
"""


def saudacao(msg, nome):
    print(msg, nome)


saudacao('Olá', 'Leticia')

"""
2 - Crie uma função que receba 3 números com parâmetros  e exiba a soma entre eles.
"""


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(1, 2, 3)
soma(3, 4, 5)
soma(6, 7, 8)
"""
3 - Crie uma função que receba 2 múmeros . O primeiro é um valor e o segundo um
percentual (ex. 100%). retorne (return) o valor do primeiro número somado do almento
do percentual do mesmo.
"""


def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

    ap = aumento_percentual(50, 100)
    print(ap)
    ap = aumento_percentual(100, 10)
    print(ap)
    ap = aumento_percentual(15, 100)
    print(ap)


"""
4 - Fizz Buzz  - Se o parâmetro da função for divisivel por 2, retorne fizz se o parâmentro
da função for divisivel por 5 e por 3 , retorne o FizzBuzz, caso o  contrario, retorne o número
enviado.
 """

"""
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzBuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n


print(fb(10))
"""


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzBuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n


from random import randint


for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
