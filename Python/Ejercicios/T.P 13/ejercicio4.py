a = int(input('Ingrese número "A": '))
b = int(input('Ingrese número "B": '))
c = int(input('Ingrese número "C": '))

print('OP = 1 A+B+C')
print('OP = 2 A-(B*C)')
print('OP = 3 (A*B)-C')

OP = int(input('Ingrese la opción de OP: '))

if OP == 1:
    print(a+b+c)
if OP == 2:
    print(a-(b*c))
if OP == 3:
    print((a*b)-c)