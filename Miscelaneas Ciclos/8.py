n = int(input('Ingrese un número para ver los multiplos de 5 hasta el número ha ingresar'))
for i in range(1, n +1):
    if i % 5 == 0:
        print(i,' es multiplo de 5')