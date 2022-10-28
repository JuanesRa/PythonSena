x = int(input('Ingrese el número base'))
y = int(input('Ingrese el exponente'))
i = 1
operacion = x
while (i < y):
    i += 1
    operacion *= x
print(operacion)