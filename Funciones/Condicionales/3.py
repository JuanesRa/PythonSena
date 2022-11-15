def digitosDelNumero(n):
    if n < 0 or n > 9999:
        return 'El número ingresado está fuera del rango'
    elif n <=9:
        return 'El número ingresado tiene 1 dígito'
    elif n <=99:
        return 'El número ingresado tiene 2 dígitos'
    elif n <=999:
       return 'El número ingresado tiene 3 dígitos'
    else:
        return 'El número ingresado tiene 4 dígitos'
    
print(digitosDelNumero(1234))