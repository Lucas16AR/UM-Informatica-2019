def relacion(a,b):
    x = 1
    y = (-1)
    z = 0

    if a > b :
        return x
    if a < b:
        return y
    if a == b:
        return z

num1 = 0
num2 = 0

print('A continuacion, tendra que ingresar dos números, si el primero es mayor, saldrá "1", si el segundo es mayor, saldrá "-1", si son iguales, saldrá "0"')

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

respuesta = relacion(num1, num2)

print(respuesta)