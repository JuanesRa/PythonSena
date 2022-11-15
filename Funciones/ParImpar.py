import random

def parImpar(num):
    if num % 2 == 0:
        #print('El numero',num,'es par')
        return 'es par'
    else:
        #print('El numero',num,'es impar')
        return 'es impar'
        
lista = []

for i in range(10):
    lista.append(round(random.randrange(100)))

print(lista)

for i in lista:
    print('El numero',i,parImpar(i))