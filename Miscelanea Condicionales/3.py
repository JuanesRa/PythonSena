n = int(input('Ingrese un numero de 0 a 9999'))
if n < 0 or n > 9999:
    print('El número ingresado está fuera del rango') 
elif n <=9:
    print('El número ingresado tiene 1 dígito')
elif n <=99:
    print('El número ingresado tiene 2 dígitos')
elif n <=999:
       print('El número ingresado tiene 3 dígitos')
else:
    print('El número ingresado tiene 4 dígitos')   