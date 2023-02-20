def imprimirSubcadenas(cadena):
    
    longitud = len(cadena)
    
    for i in range(1,longitud):
        print(cadena[0:i+1])
        
imprimirSubcadenas('Transformers')