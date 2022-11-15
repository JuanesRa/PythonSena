import random

vector = []
rango = round(random.randint(10,25))

def generarLista():
    for i in range(rango):
        vector.append(round(random.randint(1,100)))
    return 'Se generaron',rango,'numeros aleatorios que son',vector


def contarPrimos(vector):
    cont = 0
    cont2 = 0
    
    for i in range(rango):
        for n in range(2,vector[i]):
            if vector[i] % n == 0:
                cont += 1
        
        if cont <= 0:
            cont2 += 1
            print('El número',vector[i],'es primo')
        
    return 'En total hay',cont2,'numeros primos'

print(generarLista())
print(contarPrimos(vector))