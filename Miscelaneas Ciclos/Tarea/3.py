#3.numeros de 3 digitos donde la suma del cubo de cada digito sea igual al numero.

n = int(input('Ingrese un número de 3 digitos'))
x = n
while n > 99 and n < 1000:
    u = n % 10
    n = n // 10
    d = n % 10
    n = n // 10
    cubo_u = pow(u, 3)
    cubo_d = pow(d, 3)
    cubo_c = pow(n, 3)
    sumaCubos = cubo_u + cubo_d + cubo_c
    if sumaCubos == x:
        print('La suma de los cubos',n,d,u,'es',sumaCubos,'que es igual al número ingresado')
    else:
        print('La suma de los cubos',n,d,u,'es',sumaCubos,'que NO es igual al número ingresado')