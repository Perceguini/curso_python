"""
Documentações e funções built-in úteis.
"""

num1 = input('digite um numero:  ')
num2 = input('digite outro numero:  ')

# isnumeric isdigit isdecimal

# números e positivos (123456)
print(num1.isdecimal())
print(num2.isdecimal())

num1 = input('digite um numero:  ')
num2 = input('digite outro numero:  ')

print(num1 + num2)

if num1.isdigit() and num2.isdigit():

    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

else:
    print('Não pude conter numeros para letras')
