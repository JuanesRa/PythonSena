def sumaCodigos():
    
    suma = 0
    palabra = input('Ingrese una cadena para sumar sus códigos')
    listaPalabra = list(palabra)
    for i in listaPalabra:
        ord(i)
        suma += ord(i)
    print('La suma de los codigos de la palabra', palabra, 'es', suma)
    
sumaCodigos()