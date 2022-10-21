n = 1000
cont = 0
for i in range(1, n + 1):
    sum = 0
    for j in range(1,i):
        if i%j == 0:
           sum += j
    if sum == i:
        print(i)
        cont += 1
print('Hay',cont,'números perfectos.')