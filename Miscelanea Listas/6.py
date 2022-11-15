vector = [0,1]

rango = int(input('Ingrese la cantidad que se va a repetir la serie Fibonacci'))
print('La serie Fiboncci se va a ejecutar en el rango de',rango,'repeticiones')

for i in range(2,rango):
    vector.append(vector[i-1]+vector[i-2])
print(vector)
