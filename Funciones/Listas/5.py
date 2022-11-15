import random

vector = []
rango = round(random.randint(10,25))


def generarLista():
    for i in range(rango):
        vector.append(round(random.randint(1,100)))
    return 'Se ha generado',rango,'numeros aleatorios, que son',vector


def buscarNumero(vector):
    cont = 0
    n = int(input('Ingrese un número'))
    if n in vector[:]:
        for i in range(len(vector)):
            if (n == vector[i]):
                    cont += 1
                    print('El numero ingresado',n,'se encuentra en la posicion',[i])
        return 'El numero ingresado',n,'se repite',cont,'veces.'
    else:
        vector.append(n)
        print('El numero ingresado',n,'no se encuentra en la lista, por lo cual se va a agregar')
    return vector


print(generarLista())
print(buscarNumero(vector))