def ahorcado():

    palabra = 'BICICLETA'
    palabra2 = ''
    
    intentos = 7
    
    print('DISPONES DE 7 INTENTOS PARA ADIVINAR LA PALABRA')
    print('(Las letras deben ser digitadas en mayúsculas)')
    
    while intentos > 0 :
        fallas = 0
        for letra in palabra:
            if letra in palabra2:
                print(letra,end = '')
            else:
                print('-',end = '')
                fallas += 1
                
        if fallas == 0:
            print('\nFelicitaciones, has adivinado la palabra')
            break

        letra = input('\nIngresa una letra: ')
        palabra2 += letra

    
        if letra not in palabra:
            intentos = intentos - 1
            print('La letra ingresada no se encuentra en la palabra a adivinar')
            print('Te quedan',intentos,' intentos')

    
        if intentos == 0:
            print('GAME OVER')
            print('Agotaste todos los intentos')

    
    
ahorcado()