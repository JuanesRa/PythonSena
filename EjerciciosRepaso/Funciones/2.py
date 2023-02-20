#Buscar los divisores de un número ingresado por teclado

def divisores(numero):
    
    cont = 0
    for divisor in range(1, numero+1):
        if (numero % divisor) == 0 :
            print(divisor,"es divisor")
            cont += 1
    return "El numero ",numero," tiene ",cont," divisores"

n = int(input('Ingrese un número para ver los divisores hasta el número ingresado'))
divisores(n)