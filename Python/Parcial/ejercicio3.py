print('Hola usuario, aqui crearemos una matriz')

matriz = ([[1,2,3],[4,5,6],[7,8,9]])
matrizCeros = ([[1,2,3],[4,5,6],[7,8,9]])
num1 = 0
num2 = 0

for i in range (0,3):
    add = int(input('Ingrese un número para agregar a su matriz: '))
    matriz[num1][num2] = add
    matrizCeros[num1][num2] = add
    num2 = num2 + 1
num2 = 0
num1 = 1

for i in range(0,3):
    add = int(input('Ingrese un número para agregar a su matriz: '))
    matriz[num1][num2] = add
    matrizCeros[num1][num2] = add
    num2 = num2 + 1
num2 = 0
num1 = 2

for i in range(0,3):
    add = int(input('Ingrese un número para agregar a su matriz: '))
    matriz[num1][num2] = add
    matrizCeros[num1][num2] = add
    num2 = num2 + 1
num1 = 0
num2 = 0

for i in range (0,3):
    matrizCeros[num1][num2] = 0
    num1 = num1 + 1
    num2 = num2 + 1
    
print('Su matriz original es: ', matriz)
print('Su matriz resultante es: ', matrizCeros)

print('Gracias por usar nuestro sistema')