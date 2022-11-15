import random


board = []

for i in range(3):
    board.append([])
print(board)

#LISTA ANIDADA POR COMPRENSION

board = [[] for i in range(3)]
print(board)
"""
lista =  [(round(random.random()*100)) for i in range(10)]
print(lista)
par = [i for i in lista if i % 2 == 0]
impar = [i for i in lista if i % 2 != 0]
print(par)
print(impar)

parimpar = ['impar' if x % 2 == 0 else x for x in lista]

print(parimpar)"""