# Geradores, interadores e iteraveis em python

import sys
import time

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

for v in l2:
    print(v)
#Simplificando: a melhor forma de criar um gerador de forma rápida e fazer
#a troca da list Comprehension seria trocar os colchetes para parênteses.