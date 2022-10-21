numero = int(input('Ingrese un número para saber si es primo'))
contador = 0

for n in range(2,numero):   
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El número es primo")