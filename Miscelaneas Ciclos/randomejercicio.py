import random

vector = []

tam = int(input('Ingrese un numero'))

for i in range(tam):
    vector.append(round(random.random()*100))

print(vector)

conti = 0
contp = 0
sumap = 0
sumai = 0
promp = 0
promi = 0

for i in range (tam):
    #print('Posicion',i,' elemento',vector[i])
    if vector[i] % 2 == 0:
        print('El número',vector[i],'es par')
        contp+=1
        sumap += vector[i]
        promp = sumap//contp

    else:
        print('El número',vector[i],'es impar')
        conti+=1
        sumai += vector[i]
        promi = sumai//conti

print('La suma de los numeros pares es',sumap,'La suma de los numeros pares es',sumai)        
print('En total hay',contp,'numeros pares y',conti,' numeros impares')
print('El promedio de la suma de los numeros pares es',promp, 'El promedio de la suma de los numeros pares es',promi)
