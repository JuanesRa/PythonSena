#El ejercicio es mio

import random

mediana = 0

vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))


vector.sort()
if rango % 2 > 0:
    mediana = vector[rango//2]
else:
    n1 = vector[rango//2]
    n2 = vector[rango//2 - 1]
    mediana = (n1 + n2) / 2


print(vector)
print('La mediana de los números generados es',mediana)