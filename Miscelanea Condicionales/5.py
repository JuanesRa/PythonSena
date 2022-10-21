print('El juego de respuestas está a punto de comenzar...Responda con "Si", si la afirmación es correcta. Si la afirmación es incorrecta responda con "No"')
p1 = input(print('¿Colon descubrió América?'))
if p1 == 'Si':
    print('Respuesta correcta')
    p2 = input(print('¿La independencia de Colombia fue en el año 1810?'))
    if p2 == 'Si':
        print('Respuesta correcta')
        p3 = input(print('¿The Doors fue un grupo de rock Americano?'))
        if p3 == 'Si':
            print('Respuesta correcta')
            print('¡Felicitaciones, ha ganado el juego de preguntas!')
        else:
            print('Respuesta incorrecta')
            print('Juego terminado')
    else:
        print('Respuesta incorrecta')
        print('Juego terminado')
else:
    print('Respuesta incorrecta')
    print('Juego terminado')
