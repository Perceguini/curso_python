# Compreensão de dicionários em python

# l1 = [1, 2, 3, 4, 5, 6]
# ex1 = [v * 2 for v in l1]

# print(ex1)

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),

]
# d1 = {x: y * 2 for x, y in enumerate(range(5))}
d1 = {f'chave_{x}': x ** 2 for x in range(5)}
print(d1)
