r = 0
n = int(input('Ingrese un número de hasta 9 cifras'))
while n != 0:
    c = n % 10
    r = r * 10 + c
    n = n // 10
print(r)
