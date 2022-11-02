import random

cont = 0
suma = 0
promedio = 0

vector = []

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
    cont += 1
    suma += vector[i]
    promedio  = suma / cont

print('Se generaron',rango,'numeros aleatorios que son',vector)
print('La suma de los números generados es',suma)
print('El promedio de los números generados es',promedio)