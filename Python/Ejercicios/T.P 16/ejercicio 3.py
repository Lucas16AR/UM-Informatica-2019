import numpy as np

matriz = []
traza = []

for i in range (3):
    matriz.append([3] * 3)

for f in range (3):
    for c in range (3):
        add = int(input('Ingrese elemento a agregar: '))
        matriz[f][c] = add
        if f == c:
            traza.append(add)

a = np.array(matriz)
print('Su matriz es:', a)
print('La traza de su matriz es:', sum(traza))
