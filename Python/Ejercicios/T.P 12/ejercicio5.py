n = int(input('Ingrese cantidad de paquetes: '))
mayor = 0
menor = 999999
for i in range (1, n+1):
    print('Ingrese el peso')
    peso=int(input())
    suma=0
    suma=suma+peso
    if peso>mayor:
        mayor=peso
    if peso<menor:
        menor=peso
promedio=suma/n
print('El promedio es:' , promedio)
print('El peso mayor es:' , mayor)
print('El peso menor es:' , menor)