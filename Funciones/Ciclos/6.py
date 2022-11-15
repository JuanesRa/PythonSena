def numeroMayor():
    cont = 0
    max = 0
    n = 0
    
    while n >= 0:
        n = int(input('Ingrese numeros')) 
        if n > max:
            max = n
            
    return 'El mayor numero es',max

print(numeroMayor())