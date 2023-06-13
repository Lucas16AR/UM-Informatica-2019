from random import*
import numpy as np
valorLista = []
repetida = 0
matriz = []

for i in range (4):
    matriz.append([4] * 4)

for f in range (4):
    for c in range (4):
        add = randint(0,9)
        matriz[f][c] = add

a = np.array(matriz)
print(a)

valor = int(input('Ingrese un valor de una sola cifra: '))
valorLista.append(valor)
largo = len(valorLista)
if largo == 1:
    for f in range (4):
        for c in range (4):
            comparativa = matriz[f][c]
            if comparativa == valor:
                repetida = repetida + 1
    print('La cantidad de veces que su valor se repite a lo largo de la matriz es:', repetida)

else:
    print('Error reinicie el programa y ingrese un valor de una sola cifra')

