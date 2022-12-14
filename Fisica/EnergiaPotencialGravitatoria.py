"""Realice un programa que encuentre la enrgía potencial gravitatoria de un cuerpo de n kg
de masa que se encuentre a n metros de altura"""

def poencialGravitatoria():
    g = 9.8
    m = float(input('Ingrese la masa del cuerpo'))
    h = float(input('Ingrese la altura donde se encuentra el cuerpo'))
    Ep = m * g * h
    print('La energía potencial gravitatoria es de',Ep,'J')

poencialGravitatoria()

