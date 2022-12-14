#El ejercicio es mío

import random


cont = 0
suma = 0
acum = 0
promedio = 0
desEstandar = 0

vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
    cont += 1
    suma += vector[i]
    promedio  = suma / cont

    """ Desviación estandar"""
    a = int((vector[i]) - promedio)**2 / cont
    acum = acum + a
    desEstandar = (int(acum)**0.5)
    
print(vector)
print('La desviación estandar de los números generados es',desEstandar)