import random

cont = 0
cont2 = 0
vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))

    for n in range(2,vector[i]):   
      if vector[i] % n == 0:
        cont +=1

    if cont <= 0 :
      cont2 += 1
      print('El número',vector[i],'es primo')

print('En total hay',cont2,'numeros primos')
print('Se generaron',rango,'numeros aleatorios que son',vector)