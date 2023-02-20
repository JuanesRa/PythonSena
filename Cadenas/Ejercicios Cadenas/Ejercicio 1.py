def buscarRepetidas(palabra):
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    palabra2 = []
    cont = 0
    
    cadena = list(palabra)
    
    for letra in palabra:
        if letra not in palabra2:
            palabra2.append(letra)
            x = len(palabra2)
    print('En la cadena',palabra, 'se encuentran',x,'letras del abecedario')
    print(palabra2)
                
print(buscarRepetidas('Barcelona'))