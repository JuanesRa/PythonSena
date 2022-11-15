def invertirNumero(n):
    r = 0
    while n != 0:
        c = n % 10
        r = r * 10 + c
        n = n // 10

    return r

print(invertirNumero(1234))     