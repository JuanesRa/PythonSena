#Realice un programa en el cual se halle la potencia que requiere una grúa para levantar n cantidad de carga en kilogramos a n altura en metros en n tiempo en segundos.

def grua():
    g = 9.8
    
    kg = float(input('Ingrese el peso en kilogramos de la carga a levantar '))
    m = float(input('Ingrese la altura en metros que va a levantar la grua '))
    s = int(input('Ingrese el tiempo en segundos en el cual se debe levantar la carga '))

    F = kg * g
    W = F * m
    p = W/s
    
    #print('La fuerza necesaria para levantar la carga es ',F,' newtons')
    #print('El trabajo necesario para desplazar la carga es ',W,' jules')
    print('\nLa potencia necesaria del motor de la grúa para levantar',kg,'kilogramos a una altura de',m,'metros en',s,'segundos es',p,'watts')
    
grua()