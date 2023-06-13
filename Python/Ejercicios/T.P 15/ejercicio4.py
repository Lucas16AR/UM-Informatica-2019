import numpy as np
from random import*

list = []

for i in range(5):
    add = randint(0, 9)
    list.append(add)

mostrar = np.array(list)

print(mostrar)