import random

def llenarLista(lista):
    rango = round(random.randint(5,15))
    for i in range(rango):
        lista.append(round(random.randint(5,15)))
    return lista

def sumaLista(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

lista = []
print(llenarLista(lista))
print(sumaLista(lista))