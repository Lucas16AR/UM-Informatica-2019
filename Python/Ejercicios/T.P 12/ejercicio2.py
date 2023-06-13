KWconsumidos = int(input('Ingrese la cantidad de KW consumidos: '))
precio=1.20
Subtotal= KWconsumidos*precio
if KWconsumidos>700:
    porcentaje= Subtotal/100
    porcentaje2= porcentaje*5
    Total=Subtotal+porcentaje
    print('El precio es de' , Total)
    print('Se la anadio un 5% por superar los 700 KWS de consumo')
else:
    print('El precio es de' , Subtotal)