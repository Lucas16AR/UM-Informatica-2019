import numpy as np
lista = []

n = int(input('Ingrese cuantos promedios desea ingresar: '))

for i in range(n):
    x = int(input('Ingrese un promedio: '))
    lista.append(x)
np.sort(lista)

print(lista[0:5])
