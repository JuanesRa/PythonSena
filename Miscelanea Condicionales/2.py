from re import A
from traceback import print_tb


a = int(input('Ingrese el valor del primer número'))
b = int(input('Ingrese el valor del segundo número'))
c = int(input('Ingrese el valor del tercer número'))

if a == b & b == c:
    print('Los tres números son iguales')
elif a == b or b == c or c == a:
    print('Hay dos números iguales')
else:
    print('Todos los números son diferentes')