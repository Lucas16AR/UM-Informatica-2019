def area(a,b):
    x= ((a*b)/2)
    return x

num1 = 0
num2 = 0

print('Ingresara dos números para averiguar el area de un rectángulo')

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

respuesta = area(num1, num2)

print(respuesta)