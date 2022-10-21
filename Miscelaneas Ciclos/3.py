numero = int(input('Ingrese un número para saber si es perfecto'))
contador = 0
suma = 0

for n in range(1,numero):   
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
    suma = suma + n

if suma == numero:
    print('El número',numero,'es perfecto')
else:
    print('El número',numero,'no es perfecto, ya que la suma de sus divisores da',suma)