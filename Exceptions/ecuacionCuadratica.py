def ecuacionCuadratica():
    
    while True:
        try:
            a = float(input('Ingrese el valor de a: '))
            b = float(input('Ingrese el valor de b: '))
            c = float(input('Ingrese el valor de c: '))
        except:
            print('Valores incorrectos')
            
        try:
            x_1 = (-b + (b**2 -4*a*c)**0.5)
            x_2 = (-b - (b**2 -4*a*c)**0.5)


            x_1 = x_1 / (2 * a)
            x_2 = x_2 / (2 * a)

        except ZeroDivisionError:
            print('La ecuacion no puede dividirse por 0')
        
        break


    while True:
            print ("\t1 - Ecuación positiva")
            print ("\t2 - Escuación negativa")
        
            opcion = int(input("Seleccione una opción"))
    
            match opcion:
                case 1:
                    print('El resultado de la operacion positiva es ', x_1)
                case 2:
                    print('El resultado de la operacion negativa es ', x_2)

                case 0:
                    break            
        
ecuacionCuadratica()
