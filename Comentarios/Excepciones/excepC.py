def try_syntax(numerator, denominator): #Incia una funcion con dos paramentros. numerator y denominator
    try: #Incia el bloque try
        print(f'In the try block: {numerator}/{denominator}') #Imprime una cadena con las variables indicadas antes
        #quiero ver el resultado de la operacion en el print ###Tarea a relizar
        print(f'In the try block: {numerator}/{denominator} the division result is {numerator/denominator}') #Linea que imprime el resultado de la operacion, solicitado en la linea 4. En esta se hace antes de que la variable result guarde la operacion a realizar
        result = numerator / denominator #Variable result guarda el resultado de la division entre numerator y denominator
        print(f'In the try block: {numerator}/{denominator} the division result is {result}') #Linea que imprime el resultado de la operacion, solicitado en la linea 4. En esta opcion es despues de que result ya se declaró a diferencia del codigo de la linea 5
    except ZeroDivisionError as zde: #Empieza la excepcion de ZeroDivisionError, se le da el alias de zde
        print(zde) #Imprime la excepcion
    else: #El else da a entender que si la excepcion no se cumple, o sea la division se puede hacer de manera correcta, va a realizar lo siguiente
        print('The result is:', result) #Imprime cadena con la variable result que almancenó previamente la operacion
        return result #Returna variable result
    finally: #Finally valga la redundancia al final, se ejecuta sin importar si el bloque try obtuvo o no el error
        print('Exiting') #Imprime cadena
        #return "Fallo por zero" #Comentario de return
print(try_syntax(12, 4)) #Imprime la funcion dandole como paramentros 12 al numerador y 4 al denominador
print(try_syntax(11, 'a')) #Imprime la funcion dandole como paramentros 12 al numerador y 'a' al denominador que es cadena. Causando el error de TypeError 