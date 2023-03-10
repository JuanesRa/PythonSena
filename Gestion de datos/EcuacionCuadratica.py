a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))


x_1 = (-b + (b**2 -4*a*c)**0.5)/(2*a)
x_2 = (-b - (b**2 -4*a*c)**0.5)/(2*a)


print(x_1)
print(x_2)