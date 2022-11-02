import random

sumaPar = 0
sumaImpar = 0
contImpar = 0
vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))

print('Se generaron',rango,'numeros aleatorios que son',vector)

for j in (vector):
    if j % 2 == 0:
        sumaPar += j
    elif j % 2 != 0:
        contImpar += 1
        sumaImpar += j
        promedioImpar = sumaImpar / contImpar

print('La suma de numeros pares es',sumaPar)
print('El promedio numeros impares es',promedioImpar)