# add (adiciona), update(atualiza), clear, discard
# Union | (une).
# intersection & (todos os elementos presentes nos dois sets).
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão os dois sets, mas não em ambos).
"""
s1 = set()
s1.add(1)
s1.add(2)
#s1.add((1, 2, 3, 'Leticia'))
s1.discard(2)

print(s1)
"""
"""
s1 = set()
s1.update('python')

print(s1)
"""
"""
l1 = (1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 'Leticia', 'Leticia')
l1 = set(l1)
l1 = list(l1)

print(l1 [- 1])
"""
"""
s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4, 5, 6, 7}
s3 = s1 | s2

print(s3)
"""
"""
s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4, 5, 6, 7}
s3 = s1 & s2

print(s3)
"""
"""
s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {1, 2, 3, 4, 5, 6, 7}
s3 = s1 - s2

print(s3)
"""
"""
s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {1, 2, 3, 4, 5, 6, 7}
s3 = s1 ^ s2

print(s3)
"""
"""
l1 = ['leticia', 'Maria', 'João']
l2 = ['João', 'Maria', 'Maria',
      'leticia', 'leticia', 'leticia', 'leticia']

l1 = set(l1)
l2 = set(l2)

print(l1 == l2)
"""

l1 = ['leticia', 'Maria', 'João']
l2 = ['João', 'Maria', 'Maria',
      'leticia', 'leticia', 'leticia']

if set(l1) == set(l2):
    print('L1 é igual a L2')

else:
    print('L1 é diferente de L1')
