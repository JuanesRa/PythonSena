def superarnumero(numero):
    n = 0
    suma = 0
    while (suma < numero):
        n = n + 1
        suma = 0
        for i in range(n +1):
            suma = suma + 1
    return 'El número natural minimo para superar el número ingresado es',n

print(superarnumero(45))