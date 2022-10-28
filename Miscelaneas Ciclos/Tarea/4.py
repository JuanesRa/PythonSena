"""4.Generar numero (generarlo random) y adivinarlo diciendo si cada intento es mayor o menor
que el numero. Decir cuantos numeros ingreso antes de adivinarlo"""

import random

intentos = 0
fin = 0

r = (round(random.random()*100))

while fin  == 0:
    n = int(input('Ingrese un número'))
    if n == r:
        print('¡Has adivinado el número!')
        print('Usaste',intentos,'intentos para encontrar el número',r)
        print('Gamer Over')
        fin = 1
    elif n > r:
        print('Incorrecto. Intenta nuevamente con un número menor')
        intentos = intentos + 1
    elif n < r:
        print('Incorrecto. Intenta nuevamente con un número mayor')
        intentos = intentos + 1  