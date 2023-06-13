import numpy as np
listacol = []
listafila = []
matriz = []
for i in range (3):
    matriz.append([0]*3)
for f in range(3):
    for c in range(3):
        add = int(input('Ingrese un valor a agregar a su matriz: '))
        matriz[f][c] = add
a = np.array(matriz)
print(a)
fila1 = a[0,:]
fila2 = a[1,:]
fila3 = a[2,:]
sumfil1 = sum(fila1)
sumfil2 = sum(fila2)
sumfil3 = sum(fila3)
listafila.append(sumfil1)
listafila.append(sumfil2)
listafila.append(sumfil3)
print(listafila)
col1 = a[:,0]
col2 = a[:,1]
col3 = a[:,2]
sumcol1 = sum(col1)
sumcol2 = sum(col2)
sumcol3 = sum(col3)
listacol.append(sumcol1)
listacol.append(sumcol2)
listacol.append(sumcol3)
print(listacol)