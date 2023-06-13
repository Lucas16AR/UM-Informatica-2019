addLetra = 0
num = 0
num2 = 1

n = int(input('Ingrese la cantidad de nombres para leer: '))
for i in range(1, n+1):
    nombre = str(input('Ingrese un nombre: '))
    largo = len(nombre)
    addLetra = 0
    num = 0
    num2 = 1
    for i in range (1, largo + 1):
        letra = (nombre[num : num2])
        if letra == 'a':
            addLetra = addLetra + 1
        num = num + 1
        num2 = num2 + 1
    print('La cantidad de letras "a" que tiene', nombre, 'es: ', addLetra)



