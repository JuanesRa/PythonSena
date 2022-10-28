"""2. Ternas pitagoricas. Un tringulo rectangulo puede tener lados que sean todos enteros, 
el conjunto de 3 valores enteros para los lados de un triangulo rectangulo se conoce como una 
terna pitagorica. Estos 3 lados deben satisfacer la relacion que la suma de los cuadrados de los
dos lados es igual al cuadrado de la hipotenusa. Encuentre todas las ternas pitagóricas para 
el lado 1, lado 2 y la hipotenusa, todos ellos no mayores que 500. ejemplo c=3,c=4,h=5

x = pow(33,2)
y = pow(56,2)
z = pow(65,2)
suma = x+y
print(z)
print(suma)

"""
ternas = []

for a in range(1,501):
    for b in range(1,501):
        for h in range(1,501):
            if a**2 + b**2 == h**2:
                ternas.append((a,b,h))

for t in ternas:
    print(t)