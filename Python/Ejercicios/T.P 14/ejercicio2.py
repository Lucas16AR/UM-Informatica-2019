num = 0
num2  = 1
num3 = 0

frase = str(input('Ingrese la frase que desea encriptar: '))
largo = len(frase)
fraseModificada = frase

for i in range (1, largo + 1):
    letra = (frase[num : num2]) #primera letra de la frase
    if letra == 'a': 
        fraseModificada = frase[0 : num3] + '*' + frase[num + 1 : ] #si es igual: a, la suplanta por un asterisco
        frase = fraseModificada
        num = num + 1
        num2 = num2 + 1
        num3 = num3 + 1

    if letra == 'e': 
        fraseModificada = frase[0 : num3] + '&' + frase[num + 1 : ] #si es igual: a, la suplanta por un asterisco
        frase = fraseModificada
        num = num + 1
        num2 = num2 + 1
        num3 = num3 + 1

    if letra == 'i': 
        fraseModificada = frase[0 : num3] + '#' + frase[num + 1 : ] #si es igual: a, la suplanta por un asterisco
        frase = fraseModificada
        num = num + 1
        num2 = num2 + 1
        num3 = num3 + 1

    if letra == 'o': 
        fraseModificada = frase[0 : num3] + '@' + frase[num + 1 : ] #si es igual: a, la suplanta por un asterisco
        frase = fraseModificada
        num = num + 1
        num2 = num2 + 1
        num3 = num3 + 1

    if letra == 'u': 
        fraseModificada = frase[0 : num3] + '$' + frase[num + 1 : ] #si es igual: a, la suplanta por un asterisco
        frase = fraseModificada
        num = num + 1
        num2 = num2 + 1
        num3 = num3 + 1
    
    else:
        num = num + 1
        num2 = num2 + 1
        num3 = num3 + 1

print(fraseModificada) 