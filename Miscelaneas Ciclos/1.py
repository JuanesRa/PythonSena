numero = int(input('Ingrese un número'))
contador = 0
print("Los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("El numero ",numero," tiene ",contador," divisores")