"""Realice un programa que calcule la potencia de una chica de n kg de masa que trepa por una cuerda hasta n metros de altura con
velocidad constante en 15 s"""

def grua():
    g = 9.8
    
    kg = float(input('Ingrese el peso en de la chica en kilogramos '))
    m = float(input('Ingrese la altura en metros que va a trepar '))
    s = int(input('Ingrese la velocidad constante en segundos '))

    F = kg * g
    W = F * m
    p = W/s
    
    #print('La fuerza necesaria para levantar la carga es ',F,' newtons')
    #print('El trabajo necesario para desplazar la carga es ',W,' jules')
    print('\nLa potencia necesaria es',p,'watts')
    
grua()