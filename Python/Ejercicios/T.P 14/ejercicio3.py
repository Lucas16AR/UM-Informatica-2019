num = 0
num2 = -1

concidencias = 0

palabra = str(input('Ingrese una palabra: '))

largo = len(palabra)

for i in range (1, largo + 1):
    letra = (palabra[num])
    letra2 = (palabra[num2])
    if letra == letra2:
        concidencias = concidencias + 1
        num = num + 1
        num2 = num2 - 1
    else:
        print('La palabra que ingresaste no es un palindromo')
        break

if concidencias == largo:
    print('La palabra', palabra, 'es un palindromo')

