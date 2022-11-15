import random

vector = []
moda = []
rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))

    for j in range (len(rango)):
        for k in range (len(rango)):
            if j !=  k:
                if vector[k] == vector[j] and vector[k] not in moda:
                    moda.append(vector[j])
print('La lista de numeros es:',vector)
print('La moda es',moda)