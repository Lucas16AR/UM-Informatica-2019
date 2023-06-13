n = int(input('Ingrese la cantidad de números que desea guardar: '))
listNum = []
num = 0
newListNum = []

for i in range(1, n+1):
    add = int(input('Ingrese el número que desea ingresar a la lista: '))
    listNum.append(add)

largo = len(listNum)

for i in range(1, largo+1):
    dato = listNum[num]
    paridad = (-1)**dato
    if paridad == 1:
        newListNum.append(dato)
        num = num + 1
    else:
        num = num + 1

total = sum(newListNum)
print('La suma total de los números pares de su lista es: ', total)


