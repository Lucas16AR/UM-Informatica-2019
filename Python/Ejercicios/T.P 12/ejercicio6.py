print('Para votar al Candidato 1 ingrese 1 ')
print('Para votar al Candidato 2 ingrese 2 ')
print('Para votar al Candidato 3 ingrese 3 ')
print('Para votar en Blanco ingrese 4 ')
print('Si ingresa cualquier otro digito, su voto sera nulo ')

n = int(input('Ingrese la cantidad de personas que votaran: '))

cantvoto1 = 0
cantvoto2 = 0
cantvoto3 = 0
cantvoto4 = 0
cantvoto5 = 0

for i in range(1, n+1):
    voto = int(input('Ingrese su voto: '))

    if voto == 1:
        cantvoto1 = cantvoto1 + 1
    elif voto == 2:
        cantvoto2 = cantvoto2 + 1
    elif voto == 3:
        cantvoto3 = cantvoto3 + 1
    elif voto == 4:
        cantvoto4 = cantvoto4 + 1
    elif voto >= 5:
        cantvoto5 = cantvoto5 + 1

print('La cantidad de votos que recibio el Candidato 1 son ', cantvoto1)
print('La cantidad de votos que recibio el Candidato 2 son ', cantvoto2)
print('La cantidad de votos que recibio el Candidato 3 son ', cantvoto3)
print('La cantidad de votos en Blanco son ', cantvoto4)
print('La cantidad de votos nulos son ', cantvoto5)
print('La cantidad total de votos fueron ', n)