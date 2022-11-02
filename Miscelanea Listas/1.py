import random

cont = 0
suma = 0
vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
    cont += 1
    suma += vector[i]
    promedio  = suma / cont

print('Se generaron',rango,'numeros aleatorios que son',vector)
print('El promedio es',int(promedio))

for j in vector:

    if (j == promedio):
        print('El numero',j,'es el mismo que el promedio')
    elif (j < promedio):
        print('El numero',j,'es menor al promedio que es',int(promedio))
    elif (j > promedio):
        print('El numero',j,'es mayor al promedio que es',int(promedio))
