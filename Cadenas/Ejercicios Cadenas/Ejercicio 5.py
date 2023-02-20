
def UpperLower(cadena):

    for i in range(2**len(cadena)):
        formato = formato(len(cadena))
        resultado = ''
        for j in range(len(cadena)):
            if formato[j] == '0':
                resultado += cadena[j].lower()
            else:
                resultado += cadena[j].upper()
        print(resultado)

UpperLower('cadena')