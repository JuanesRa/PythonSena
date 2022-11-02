import random


cont = 0
vector = []
vector2 = []

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))

print(vector)

n = int(input('Ingrese un número'))
vector2.append(n)

for i in vector:
    for j in vector2:
        if (i == j):
            cont += 1
            print('El numero ingresado',n,'se encuentra en la posicion',[i])
print('El numero ingresado',n,'se repite',cont,'veces.')
