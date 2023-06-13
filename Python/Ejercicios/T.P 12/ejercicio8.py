from random import*
from typing import Any, Union

salida = False
valor1 = 0
valor2 = 0
valor3 = 0
repite = 0

while not salida:
    valor1: Union[int, Any] = randint(1, 10)
    valor2 = randint(1, 10)
    valor3 = randint(1, 10)
    result1 = valor1*valor2
    result2 = valor1*valor3
    result3 = valor2*valor3

    if valor1 == result3 or valor2 == result2 or valor3 == result1:
        print('Valor igual al producto de los demas valores')
        print(valor1, valor2, valor3)
        repite = repite + 1
        print('Cantidad de repeticiones', repite)
        salida = True
