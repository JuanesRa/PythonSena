import random

vector = []
rango = round(random.randint(10,25))


def generarLista():
    for i in range(rango):
        vector.append(round(random.randint(1,100)))
        
    return 'Lista desordenada:',vector


def listaMenorAMayor(vector):
    for i in range(rango-1):
        for j in range(rango-1-i):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
                
    return 'Lista ordenada de menor a mayor:',vector


def listaMayorAMenor(vector):
    for i in range(rango-1):
        for j in range(rango-1-i):
            if vector[j] < vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
                
    return 'Lista ordenada de mayor a menor:',vector



print(generarLista())
print(listaMenorAMayor(vector))
print(listaMayorAMenor(vector))