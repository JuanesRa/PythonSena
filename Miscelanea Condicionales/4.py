c = int(input('Ingrese la calificación de 0 a 10'))
if c < 0 or c > 10:
    print('La calificación no es válida') 
elif c <=2:
    print('F, Muy deficiente')
elif c <=4:
    print('D, Deficiente')
elif c <=6:
       print('C, Suficiente')
elif c <=8:
       print('B, Satisfactorio')
else:
    print('A, Excelente')   