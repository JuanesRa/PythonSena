num1 = int(input('Ingrese el valor del numerado del primer fraccionario'))
den1 = int(input('Ingrese el valor del denomidador del primer fraccionario'))
num2 = int(input('Ingrese el valor del numerado del segundo fraccionario'))
den2 = int(input('Ingrese el valor del denomidador del segundo fraccionario'))

sumNum = num1 + num2
restNum = num1 - num2

multNum = num1 * num2
multDen = den1 * den2

divNum = num1 * den2
divDen = num2 * den1

sumDifDen = divNum + divDen
restDifDen = divNum - divDen

if den1 == den2:
    print('La suma de',num1,'/',den1,'y',num2,'/',den2,'es',sumNum,'/',den1)
    print('La resta de',num1,'/',den1,'y',num2,'/',den2,'es',restNum,'/',den1)
    print('La multiplicacion de',num1,'/',den1,'y',num2,'/',den2,'es',multNum,'/',multDen)
    print('La division de',num1,'/',den1,'y',num2,'/',den2,'es',divNum,'/',divDen)

else:
    print('La suma de',num1,'/',den1,'y',num2,'/',den2,'es',sumDifDen,'/',multDen)
    print('La resta de',num1,'/',den1,'y',num2,'/',den2,'es',restDifDen,'/',multDen)
    print('La multiplicacion de',num1,'/',den1,'y',num2,'/',den2,'es',multNum,'/',multDen)
    print('La division de',num1,'/',den1,'y',num2,'/',den2,'es',divNum,'/',divDen)