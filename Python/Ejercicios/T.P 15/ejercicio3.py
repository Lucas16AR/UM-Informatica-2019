lista = []
largo = int(input('Ingrese la longitud que tendra su lista: '))

for i in range(1, largo + 1):
    add = int(input('Ingrese un nùmero para agregar a la lista: '))
    lista.append(add)

print('El nùmero mas grande su lista es:', max(lista))
print('El nùmero mas chico de su lista es:', min(lista))
