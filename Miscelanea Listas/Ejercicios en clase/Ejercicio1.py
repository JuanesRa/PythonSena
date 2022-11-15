import random

sumaPrimera = 0
promedioPrimera = 0
sumaSegunda = 0
promedioSegunda = 0
tempDiaria = []

dias = 30


for i in range(dias):
    tempDiaria.append(random.randint(4,28))
    #print('El dia',i,'tuvo una temperatura de',tempDiaria[i]
primeraMitad = tempDiaria[:15]
segundaMitad = tempDiaria[16:]

for i in range(len(primeraMitad)):
    sumaPrimera += primeraMitad[i]
    promedioPrimera = sumaPrimera / len(primeraMitad)

#print(sumaPrimera)
print('El promedio de temperatura en la primera parte del mes fue',promedioPrimera)


for i in range(len(segundaMitad)):
    sumaSegunda += segundaMitad[i]
    promedioSegunda = sumaSegunda / len(segundaMitad)

#print(sumaSegunda)
print('El promedio de temperatura en la segunda parte del mes fue',promedioSegunda)