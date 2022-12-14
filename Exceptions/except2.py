def divisores(num):
    try:        
        for i in range(num+1):
            if num%i==0:
                print(i,' es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')

while True:
    var=int(input('ingrese numero'))
    if var is not int:
        print('El dato ingresado no es numerico')
    else:
        divisores(var)
        print('El programa continua en esta linea')
    