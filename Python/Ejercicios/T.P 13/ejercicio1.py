suma = 0.0
i = 0
menores = 0

while True:
    nota = float(input('Ingrese al sistema las notas: '))
    if nota == -1:
        break
    else:
        i += 1
        suma = suma + nota
    if 8 > nota:
        menores = menores + 1

        promedio = suma / i

print('Las notas menores de 8 son', menores)
print('El promedio de las notas es:', promedio)
