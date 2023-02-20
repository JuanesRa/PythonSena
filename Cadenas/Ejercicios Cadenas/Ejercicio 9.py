# Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.

texto = input('Escriba su palabra o frase: ').lower()
abecedario = 'abcdefghijklmnopqrstuvwxyz'
cifrado = ''
desplazamiento = 3
for i in texto:
  try:
    if i in abecedario:
      cifrado += abecedario[(abecedario.index(i))+(desplazamiento)]
    else:
      cifrado+=i
  except IndexError:
    cifrado+=i
print(cifrado)