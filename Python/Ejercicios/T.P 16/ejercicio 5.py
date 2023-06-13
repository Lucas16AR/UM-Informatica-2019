import numpy as np
import sys
matriz= []
lista = []
num = 0
listaMayor = []
filas = int(input('Ingrese la cantidad de filas que tendra su matriz: '))
columnas = int(input('Ingrese la cantidad de columnas que tendra su matriz: '))

if filas == columnas:
    for i in range(filas):
        matriz.append([0] * columnas)
else:
    print('Por favor reinicie el programa e ingrese una matriz cuadrada: ')
    sys.exit()

for f in range(filas):
    for c in range(columnas):
        add = int(input('Ingrese un numero para agregar a su matriz cuadrada: '))
        matriz[f][c] = add
        lista.append(add)
    listaMayor.append(max(lista))

a = np.array(matriz)
b = np.sum(a)
mm = np.amax(a)
c = np.sort(a)
d = np.tril(a)

print('La suma de todos los elementos de la matriz es:', b)
print('El mayor valor ingresado en su matriz es:', mm)
for i in range(filas):
    print('El valor mas grande de la fila', num, 'es: ', listaMayor[num])
    num = num + 1
print('La suma de la diagonal principal es:', np.trace(a))
print('El promedio de su matriz es:', b/len(matriz))
print('Las filas de la matriz ordenadas son:', c)
print('La matriz triangular superior es:', d)