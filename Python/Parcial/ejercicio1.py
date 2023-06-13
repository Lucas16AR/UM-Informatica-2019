print('Hola usuario, en este programa te mostrare la tabla de multiplicación del 1 al 10, de un numero que tu elijas')
x = int(input('Ingrese un número entero: '))
r = range(x, x+1)
for i in r:
    print(i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i,9*i, 10*i)