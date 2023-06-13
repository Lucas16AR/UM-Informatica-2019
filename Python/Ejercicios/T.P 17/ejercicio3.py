listaPar = []

listaImpar = []

listUno = []
largo = int(input('Ingrese la cantidad de nùmeros que tendra su lista: '))

for i in range(1, largo + 1):
    add = int(input('Ingrese un nùmero para agregar a la lista: '))
    listUno.append(add)

def separar(listUno):
    largo2 = len(listUno)
    num = 0
    for i in range(1, largo2 + 1):
        dato = listUno[num]
        paridad = (-1)**dato
        if paridad == 1:
            listaPar.append(dato)
            num = num + 1
        else:
            listaImpar.append(dato)
            num = num + 1

    print(listaPar)
    print(listaImpar)

    return listaPar
    return listaImpar
paridad = separar(listUno)