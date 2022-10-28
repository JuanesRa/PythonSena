numero = int(input('Ingrese un número'))
n = 0
suma = 0
while (suma < numero):
    n = n + 1
    suma = 0
    for i in range(n +1):
        suma = suma + 1
print('El número natural minimo para superar el número ingresado es',n)