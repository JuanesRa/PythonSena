values = (1, 0) #Values es una tupla con los valores de 1 y 0
#x,y=10,12 ###Comentario explicativo de como asignar valores a dos diferentes variables en una misma linea de codigo
#print(divmod(10,3)) ###Comentario que imprime una funcion con con los valores de 10 y 3
try: #Incia el bloque try
    q, r = divmod(*values) #Las variables q y r van a obtener los valores de la tupla resultante de la operacion divmod, el * indica que van a ser asignados solo un valor de la tupla a una variable, con el fin de que q y r no obtengan como resultado la tupla completa, ya que trendrian el mismo valor
    #print('valor de q=',q) ###Ejemplo de print que se viene trabajando
    print(f'q={q}') #Impresion de la variable q del modo que es más facil trabajar con strings y variables
    print(f'r={r}') #Impresion de la variable r del modo que es más facil trabajar con strings y variables
except (ZeroDivisionError, TypeError) as e: #Incia el except con ZeroDivisionError y TypeError, con el fin de que muestre el valor y el mensaje de error si a los valores de values se les da un string o si el divisor lleva 0. Se le asigna a estos errores el alias de e
    print(type(e), e) #En caso de que la exepcion se cumpla, va a mostrar el error y su valor