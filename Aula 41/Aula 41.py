# t1 = [1, 2, 3, 4, 5]
# print(t1[2:])


# t1 = 1, 2, 3, 'a', 'b'
# print(t1)

# t1 = 1, 2, 3, 4
# t2 = 5, 6, 7, 8
# t3 = t1 + t2
# n1, n2, n3, *_, n10 = t3

# print(n10)

# t1 = (1, 2, 'Leticia', 4, 5) * 20
# print(t1)

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)
print(t1)
