Lista = []
Cantidad = int(input('Ingrese cantidad de nùmeros que tendra su lista: '))

for i in range(1, Cantidad+1):
    valor = int(input('Ingresar valores a la lista: '))
    Lista.append(valor)

print(Lista)
print(list(set(Lista)))
