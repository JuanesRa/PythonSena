x = int(input('Ingrese la poblacion'))
y = int(input('Ingrese el incremento'))
i = x*2
while (x < i):
    pe = x * y/10
    pn = pe+x
    x = pn
    print('La poblacion incremento en',pe,'la poblacion total es',pn)