def numerosIguales(a,b,c):
    if a == b & b == c:
        return 'Los tres números son iguales'
    elif a == b or b == c or c == a:
        return 'Hay dos números iguales'
    else:
        return 'Todos los números son diferentes'
    
print(numerosIguales(5,5,5))