import numpy as np
from random import randint

lista = []

for i in range(10):
    x = np.array(randint(0, 9), dtype=int)
    lista.append(x)
c = (randint(0, 9), int)

print(c)
x = int

for x in lista:
    if c > x:
        del lista[x]

print(lista)
