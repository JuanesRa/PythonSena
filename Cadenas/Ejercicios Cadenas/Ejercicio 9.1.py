def cifrado(cadena):
    for i in cadena:
        if ord(i) >= 33 and ord(i) <= 62:
            print((chr(ord(i)-3)), end = "")
        
        elif ord(i) >= 63 and ord(i) <= 93:
            print((chr(ord(i)-3)), end = "")
            
        elif ord(i) >= 94 and ord(i) <= 126:
            print((chr(ord(i)+3)), end = "")
            
def descifrado(cadena):
    for i in cadena:
        if ord(i) >= 33 and ord(i) <= 62:
            print((chr(ord(i)+3)), end = "")
        
        elif ord(i) >= 63 and ord(i) <= 93:
            print((chr(ord(i)+3)), end = "")
            
        elif ord(i) >= 94 and ord(i) <= 126:
            print((chr(ord(i)-3)), end = "")
            
            
cifrado('palabra')
#descifrado()
