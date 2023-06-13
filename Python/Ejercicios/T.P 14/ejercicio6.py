abc = 'abcdefghiklmnñopqrstyvwxyz'
num1 = 0
num2 = 0
tieneNumero = False
tieneLetra = False

nombreUsuario = str(input('Ingrese un nombre de usuario: '))
largo = len(nombreUsuario)
largoAbc = len(abc)

if largo > 12:
    print('El nombre de usuarios no puede contener mas de 12 caracteres')
if largo < 6:
    print('El nombre de usuario debe contener al menos 6 caracteres')
    caracterAbc = (abc[num2])

if largo >= 6 and largo <=12:
    for i in range (1, largo + 1):
        caracter1 = (nombreUsuario[num1])
        for i in range (1, largoAbc + 1):
            caracterAbc = (nombreUsuario[num2])
            if caracter1 == caracterAbc:
                tieneLetra = True
            else:
                num2 = num2 + 1
        num1 = num1 + 1


if tieneLetra == True:
    print('Nombre de usuario valido')
else:
    print('Nombre de usuario invalido')

