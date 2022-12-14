#El ejercicio es mio

"""Pedir 3 números e indicar cual de ellos es el valor medio sin usar operadores lógicos"""

n1 = int(input('Ingrese el valor del primer numero'))
n2 = int(input('Ingrese el valor del segundo numero'))
n3 = int(input('Ingrese el valor del tercero numero'))

if n1 > n2:
    if n1 < n3:
        print (n1)
if n2 >n1:
    if n2 < n3:
        print (n2)
if n3 > n1:
    if n3 < n2:
        print(n3)
if n2 < n1:
    if n2 > n3:
        print (n2)
if n1 < n2:
    if n1 > n3:
        print (n1)
if  n3 < n1:
    if n3 > n2:
        print (n3)