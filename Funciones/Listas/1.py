import random

vector = []
rango = round(random.randint(10,25))

def generarLista():
    for i in range(rango):
        vector.append(round(random.randint(1,100)))
    return vector


def promedioLista(vector):   
    cont = 0
    suma = 0
    for i in range(rango):
        cont += 1
        suma += vector[i]
        promedio = suma / cont

    print('El promedio los',len(vector),'numeros de la lista es',int(promedio))
        
    for j in vector:
        if (j == promedio):
            return 'El numero',j,'es el mismo que el promedio'
        elif (j < promedio):
            return 'El numero',j,'es menor al promedio que es',int(promedio)
        elif (j > promedio):
            return 'El numero',j,'es mayor al promedio que es',int(promedio)
    

print(generarLista())
print(promedioLista(vector))