#Crear un programa que agregue a una lista cierta cantidada de numeros pares.

def agregarPares(numero):
    
    lista = [0,1,3,5]
    
    for i in range(1,numero+1):
        if i % 2 == 0:
            lista.append(i)
    print(lista)


n = int(input('Ingrese un número para ver los numeros pares hasta el número ingresado'))
agregarPares(n)