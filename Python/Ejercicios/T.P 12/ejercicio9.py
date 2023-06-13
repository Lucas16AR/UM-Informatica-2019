tamanoPizza = 0
carrito = 0
addCarrito = 0
ingredientes = 0

print('Bienvenido al servicio de pedidos de pizza UM')
print('A continuacion verá el menu y los precios')
print('Opción 1: Pizza pequeña $250')
print('Opción 2: Pizza mediana $300')
print('Opción 3: Pizza grande $380')
print('Además le puede agregar ingredientes adicionales por $30 c/u, tales como: ')
print('Opción a: Huevo frito y rodajas de Salame')
print('Opción b: Blue Cheese y Albaca')
print('Opción c: Aceitunas y Sardinas')
print('Opción d: Jamon Crudo y Aceitunas')
print('A continuacion por favor ingrese la opcion de la pizza y luego la opcion de los ingredientes extras. En caso de no querer ningun ingrediente extra solo eliga la "Opcion 0')

tamanoPizza = int(input('Ingrese la opcion de la pizza '))
if tamanoPizza == 1:
    carrito = 250
if tamanoPizza == 2:
    carrito = 300
if tamanoPizza == 3:
    carrito = 380

ingredientes = str(input('Ingrese la opcion de ingrediente extra o ponga "x" si no quiere ninguno '))

if ingredientes == 'a':
    add = 'huevo frito y rodajas de salame'
    addCarrito = 30
    print('Usted eligio la opcion ', tamanoPizza, 'mas la opcion de ingredientes', add, 'total a pagar: ',
          carrito + addCarrito)

if ingredientes == 'b':
    add = 'blue cheese y albaca'
    addCarrito = 30
    print('Usted eligio la opcion ', tamanoPizza, 'mas la opcion de ingredientes', add, 'total a pagar: ',
          carrito + addCarrito)
if ingredientes == 'c':
    add = 'aceitunas y sardinas'
    addCarrito = 30
    print('Usted eligio la opcion ', tamanoPizza, 'mas la opcion de ingredientes', add, 'total a pagar: ',
          carrito + addCarrito)

if ingredientes == 'd':
    add = 'jamon crudo y aceitunas'
    addCarrito = 30
    print('Usted eligio la opcion ', tamanoPizza, 'mas la opcion de ingredientes', add, 'total a pagar: ',
          carrito + addCarrito)

if ingredientes == 'x':
    print('Usted eligio la opcion', tamanoPizza, 'total a pagar: ', carrito)