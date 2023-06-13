print('Hola usuario, por favor ingresa números enteros para crear una lista, para terminar introduce el cero')
list = []
add = 1
sumatoria = 0
num1 = 0

while add != 0:
    add = int(input('Ingrese un numero para ser agregado a la lista '))
    list.append(add)

print('La cantidad de números que hay en la lista es:', len(list))
print('El número más grande su lista es:', max(list))
print('La lista ordenada de mayor a menor es: ', sorted(list))
largo = len(list)
for i in range (1, largo + 1):
    sumatoria = sumatoria + list[num1]
    num = num1 + 1

promedio = sumatoria/(largo - 1)
print('El promedio de su lista es:', promedio)
print('Gracias por usar nuestro sistema')