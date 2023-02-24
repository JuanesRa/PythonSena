def edad(): #Inicia funcion edad
    try: #Incia bloque try
        tuedad=int(input("introduce tu edad")) #La variable tuedad se convierte a entero y guarda un valor ingresado por teclado
        print(f'tu edad es  {tuedad}') #Imprime una cadena con la variable tuedad
        #print('Tu edad es ',tuedad) #Ejemplo de impresion que se viene trabajando
    except ValueError as e: #Incia la excepcion de ValueError y se le asigna el alias de e
        print(e) #Imprime el error, bajo el alias de e
        print("La edad debe ser un valor numerico...") #Imprime cadena solicitando que se ingrese un valor numerico
        edad() #Llama a la funcion edad nuevamente, para que solo se logre finalizar hasta que se ingrese un valor numerico
    
edad() #Llamado de la funcion