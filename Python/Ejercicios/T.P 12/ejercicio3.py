a = float(input('Ingrese un lado del triángulo: '))
b = float(input('Ingrese otro lado del triángulo: '))
c = float(input('Ingrese otro lado del triángulo: '))
if (a==b==c):
    print('El triángulo es equilatero')
elif (a==c or a==b or c==b):
    print('El triángulo es isósceles')
else:
    print('El triángulo es escaleno')
