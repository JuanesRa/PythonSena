cont = 0
max = 0
n = int(input('Ingrese numeros')) 
while n >= 0:
    n = int(input('Ingrese numeros')) 
    if n > max:
        max = n
    
print('El mayor numero es',max)
