def calificacion(c):
    if c < 0 or c > 10:
        return 'La calificación no es válida'
    elif c <=2:
        return 'F, Muy deficiente'
    elif c <=4:
        return 'D, Deficiente'
    elif c <=6:
        return 'C, Suficiente'
    elif c <=8:
        return 'B, Satisfactorio'
    else:
        return'A, Excelente'
    
print(calificacion(10))