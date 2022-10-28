#1. pedir numeros, imprimirlo con el opuesto, finaliza con cero y diga cuantos ingreso

cont = 0
n = int
while n != 0:
    n = int(input('Ingrese numeros'))
    cont = cont+1
    if n > 0:
        x = n*(-1)
        print(x)
    else:
        x = n*(-1)
        print(x)
print('El total de numeros ingresados es de',cont)