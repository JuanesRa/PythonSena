import random


cont = 0
vector = []

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
print(vector)

n = int(input('Ingrese un número'))

if n in vector[:]:
    for i in range(len(vector)):
        if (n == vector[i]):
                cont += 1
                print('El numero ingresado',n,'se encuentra en la posicion',[i])
    print('El numero ingresado',n,'se repite',cont,'veces.')
else:
    vector.append(n)
    print('El numero ingresado',n,'no se encuentra en la lista, por lo cual se va a agregar')
print(vector)