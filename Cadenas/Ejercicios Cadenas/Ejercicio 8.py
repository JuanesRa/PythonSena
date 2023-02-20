def buscarRepetidas(palabra):
    consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vocales = ['a','e','i','o','u']
    vocalesConTilde = ['á','é','í','ó','ú']
    consonantesCadena = []
    vocalesCadena = []
    vocalesCadenaTildes = []
    
    cadena = list(palabra)
    
    for letra in palabra:
        if letra in consonantes:
            consonantesCadena.append(letra)
            x = len(consonantesCadena)

            print('En la cadena',palabra, 'se encuentran',x,'consonantes')
            print(consonantesCadena)

        if letra in vocales:
            vocalesCadena.append(letra)
            x = len(set(vocalesCadena))

            print('En la cadena',palabra, 'se encuentran',x,'vocales')
            print(vocalesCadena)

        if letra in vocalesConTilde:
            vocalesCadenaTildes.append(letra)
            x = len(set(vocalesCadenaTildes))
            
            print('En la cadena',palabra, 'se encuentran',x,'vocales con tíldes')
            print(vocalesCadenaTildes)

                
print(buscarRepetidas('Barcelona'))