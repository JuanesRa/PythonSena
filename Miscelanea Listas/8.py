import random


cont = 0
moda = 0
mayor = 0
vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))

for i in range(r):

    cont = 0

    for j in range(r):
        if(vector[i] == vector[j]):
            cont += 1

    if (cont > mayor):
        mayor = cont
        moda = vector[i]

print('La moda es',moda,'y se repite',mayor,'veces')
print('Se generaron',rango,'numeros aleatorios que son',vector)