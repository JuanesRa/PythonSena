lista = [1,1,9,7,3,4,8,1,4,9,7,8,4,2,64,1215,45,321,84,321,5,1,64,]
lista2 = []

for i in lista:
    if i not in lista2:
        lista2.append(i)

print(lista)
print(lista2)