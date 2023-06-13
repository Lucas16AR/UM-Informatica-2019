import numpy as np
matriz = []

for i in range(4):
    matriz.append([0] * 3)

for i in range(4):
    for j in range(3):
        add = i+j
        matriz[i][j] = add

a = np.array(matriz)
print(a)
