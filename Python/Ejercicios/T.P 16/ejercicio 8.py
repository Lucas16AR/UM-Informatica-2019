import numpy as np
lista=[]
lista2=[]
num2=(-1)
matriz=[]
sumaTotal= 0
for i in range (4):
    matriz.append([0]*4)
for f in range (4):
    for c in range (4):
        add = int(input('Ingrese elemento a agregar: '))
        matriz2[f][c] = add
        sumaTotal = sumaTotal + add
        lista.append(add)
    lista2.append(lista[num2])
    num2 = num2 - 1

a = np.array(matriz)
print(a)
sumdiag = np.trace(a)
if sumdiag == sum(lista2):
    print('Esta matriz es semi magica')