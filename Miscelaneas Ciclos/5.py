n = 1000
cont = 0
for i in range(2, n + 1):
    primos = True
    for j in range(2,i):
        if i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(i)
        cont += 1
print('Hay',cont,'números primos.')