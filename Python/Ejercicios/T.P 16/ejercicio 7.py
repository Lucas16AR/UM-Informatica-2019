import numpy as np

filas = int(input('Ingrese la cantidad de filas que tendra su matriz: '))
columnas = int(input('Ingrese la cantidad de columnas que tendra su matriz: '))
matriz = []
matriz2 = []
for i in range(filas):
    matriz2.append([0] * columnas)
for i in range(filas):
    matriz.append([0] * columnas)

for f in range(filas):
    for c in range(columnas):
        add = int(input('Ingrese un valor para agregar a su matriz: '))
        matriz[f][c] = add

print('Opcion 1 para obtener el determinante de su matriz')
print('Opcion 2 para obtener la matriz traspuesta')
print('Opcion 3 para sumar otra matriz que tendra que ingresar')
print('Opcion 4 para mostrar la matriz con la diagonal principal llena de ceros')
opcion = int(input('Ingrese una opcion: '))

if opcion == 1:
    a = np.array(matriz)
    b = np.linalg.det(a)
    print(b)
if opcion == 2:
    a = np.array(matriz)
    b = np.transpose(a)
    print(b)
if opcion == 3:
    for f in range(filas):
        for c in range(columnas):
            add = int(input('Ingrese un valor para agregar a su  nueva matriz: '))
            matriz2[f][c] = add
    a = np.array(matriz)
    b = np.array(matriz2)
    c = (a+b)
    print(c)
if opcion == 4:
    a = np.array(matriz)
    np.diag(a) * 0
    print(a)