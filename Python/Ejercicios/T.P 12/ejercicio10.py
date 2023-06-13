bacterias = int(input('Ingrese la cantidad de bacterias: '))
max = int(input('Ingrese la cantidad maxima de bacterias: '))
dias = 0

while bacterias < max:
    bacterias = bacterias*2
    dias = dias + 1

print('La cantidad de dìas que se necesitan para que sus bacterias sobrepasen el màximo es:', dias, 'dìas')