import numpy as np
import sys
sumaTotal = 0
matriz = []
traza = []
trazaNegativa = []
num = 4
lista = []
lista2 = []
num2 = (-1)

orden = int(input('Ingrese el numero de filas que tendra su matriz: '))
orden2 = int(input('Ingrese el numero de columnas que tendra su matriz: '))

if orden == orden2:

    for i in range (orden):
        matriz.append([orden] * orden2)

    for f in range (orden):
        for c in range (orden2):
            add = int(input('Ingrese elemento a agregar: '))
            matriz[f][c] = add
            sumaTotal = sumaTotal + add
            if f == c:
                traza.append(add)
            lista.append(add)
        lista2.append(lista[num2])
        num2 = num2 - 1
else:
    print('Reinicie el programa y ingrese una matriz cuadrada por favor')
    sys.exit()




diferencia = sumaTotal - sum(traza)
diferencia = diferencia - sum(lista2)
a = np.array(matriz)
print('Su matriz es:', a)
print('La suma total de todos sus elementos de la matriz menos las diagonales es:', diferencia)

