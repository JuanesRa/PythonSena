def sumaDivisores(num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum += i
    return sum


def numeroPerfecto(n):
    suma = sumaDivisores(n)
    if n == suma:
        return 'es perfecto'
    else:
        return 'no es perfecto'
    
def numeroPrimo(n):
    suma = sumaDivisores(n)
    if suma == 1:
        return 'es primo'
    else:
        return 'no es primo'
    
    
def amigos(x,y):
    sumx = sumaDivisores(x)
    sumy = sumaDivisores(y)
    if sumx == y and sumy == x:
        return 'son amigos'
    else:
        return 'no son amigos'
    
print('La suma de los divisores es',sumaDivisores(10))
print('El numero',numeroPerfecto(10))
print('El numero',numeroPrimo(10))
print('El numero',amigos(220,284))