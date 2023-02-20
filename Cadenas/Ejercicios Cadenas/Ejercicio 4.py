def buscarRepetidas(palabra):
    
    cadena = list(palabra)
    
    for letra in palabra:
        repeticiones = cadena.count(letra)
        print('El carácter',letra,' se repite', repeticiones, 'veces en la cadena ',palabra)
                
print(buscarRepetidas('Abecedario'))