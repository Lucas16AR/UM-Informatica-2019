import numpy as np
lista = []

n = int(input('Ingrese la cantidad de nùmeros que desea ingresar: '))

for i in range(n):
    x = int(input('Ingrese un nùmero: '))
    lista.append(x)

print(np.sum(lista))
print(np.sum(lista)/n)
print(np.sum(lista)**2)
print(np.sum(lista)**3)
