"""
Manipulando strings - Aula 6
* String indices
* fatiamento de stringns [inicio:fim:passo]
* funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
Pode ser comferido em:
https://docs.python.org/3/library/stdtypes.html
"""
# Positivos [012345678]
texto = 'python_s2'
# Negativos -[987654321]
print(texto[8])

nova_string = texto[0::3]
print(nova_string)
print(len(texto))
