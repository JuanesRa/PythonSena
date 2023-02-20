def buscarRepetidas(palabra):
    consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vocales = ['a','e','i','o','u']
    vocalesConTilde = ['á','é','í','ó','ú']
    consonantesCadena = []
    vocalesCadena = []
    vocalesCadenaTildes = []
    caracterEspecial = []
    
    cadena = list(palabra)
    
    for letra in palabra:
        if letra in consonantes:
            consonantesCadena.append(letra)
            x = len(consonantesCadena)

        elif letra in vocales:
            vocalesCadena.append(letra)
            y = len(set(vocalesCadena))

        elif letra in vocalesConTilde:
            vocalesCadenaTildes.append(letra)
            z = len(set(vocalesCadenaTildes))
            
        else:
            caracterEspecial.append(letra)
            f = len(set(caracterEspecial))
            
            
    print('En la cadena',palabra, 'se encuentran',x,'consonantes')
    print(consonantesCadena)
    
    print('En la cadena',palabra, 'se encuentran',y,'vocales')
    print(vocalesCadena)
    
    print('En la cadena',palabra, 'se encuentran',z,'vocales con tíldes')
    print(vocalesCadenaTildes)
    
    print('En la cadena',palabra, 'se encuentran',f,'carácteres especiales')
    print(caracterEspecial)

                
print(buscarRepetidas('transformación.-{'))