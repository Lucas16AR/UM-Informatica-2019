def cubo(n):
    c = n**3
    return c

cant = int(input('Ingrese cantidad de valores deseados: '))

for i in range(1, cant+1):
    n = int(input('Ingrese un valor: '))
    potencia = cubo(n)
    print(potencia)