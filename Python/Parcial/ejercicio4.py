print('Hola usuario, a continuación tendras dos opciones para elegir para resolver su operación')
eleccion = int(input('1_Calculo de una potencia  o 2_ Calculo de una raiz cuadrada: '))

if eleccion == 1:
    num1 = int(input('Ingrese el número para elevar '))
    num2 = int(input('Ingrese el número exponente '))
    result1 = num1**num2
    print('El resultado de la potencia es:', result1)

if eleccion == 2:
    num1 = int(input('Ingrese el número para calcular la raiz cuadrada '))
    num2 = 0.5
    result2 = num1**num2
    print('El resultado de la raiz cuadrada es:', result2)

print('Gracias por usar nuestro sistema')