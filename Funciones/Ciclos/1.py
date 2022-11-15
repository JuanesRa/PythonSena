def divisoresXnumero(numero):
    cont = 0
    for divisor in range(1,numero+1):
        if (numero % divisor) == 0 :
            print(divisor,"es divisor")
            cont += 1
    return "El numero ",numero," tiene ",cont," divisores"
    
print(divisoresXnumero(46))