n = int(input('Ingrese el valor de n'))
for i in range(n):
    #print(n-i)
    num = 0
    for j in range(i):
        num += j
    
        print(i,j,num)
