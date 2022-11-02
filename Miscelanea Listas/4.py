import random


vector = []

rango = random.randint(10,25)

for x in range(rango):
    vector.append(round(random.random()*100))

print('Lista desordenada:',vector)

for i in range(rango-1):
    for j in range(rango-1-i):
        if vector[j] > vector[j+1]:
            vector[j], vector[j+1] = vector[j+1], vector[j]

print('Lista ordenada de menor a mayor:',vector)

for i in range(rango-1):
    for j in range(rango-1-i):
        if vector[j] < vector[j+1]:
            vector[j], vector[j+1] = vector[j+1], vector[j]

print('Lista ordenada de mayor a menor:',vector)