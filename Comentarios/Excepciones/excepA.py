try: #Inicia el bloque para realizar la prueba de su contenido
    #print(1/1)) ###Comentario en el cual hay un print con un error de sintaxis debido al parentesis de cierra pero no abre
    raise SyntaxError #Trae el error de SyntaxError
except SyntaxError as e: #Ahora trae el excpt con el SyntaxError y le pone el alias de e
    print(e) #Imprime e, que basicamente es el valor de la excpecion. Pero trae un valor de none ya que para que traiga ese valor de la excepcion se tiene que ejecutar el error y no traerlo con el raise
    print('Cierra el parentesis') #Trae un mensaje personalizado respecto a la excepcion
    
try: #Inicia el bloque para realizar la prueba de su contenido
    #raise ZeroDivisionError ### Acá trae la excepcion pero está comentada
    print(1/0) #Imprime la operacion de 1/0 con el fin de que entre a la excepcion
#except (ZeroDivisionError) as e: #Comentario de la excepcion con alias e entre paréntesis
except ZeroDivisionError as zde: # Basicamente es la misma linea de arriba pero con diferente alias y la excepcion sin estar entre paréntesis
    print(zde) #Una vez entra a la excepcion, imprime el valor de ella bajo la variable zde dada de alias en la linea de arriba
    #print('prueba error')