numero = int(input('Ingrese un valor de dos cifras: '))
decena = numero // 10
unidad = numero % 10
suma = unidad + decena

if suma % 2 == 0:
   print('El resultado es', suma, ' La suma de ambos números es un valor par')
elif suma % 2 != 0:
   print('El resultado es', suma, ' La suma de ambos números es un valor impar')