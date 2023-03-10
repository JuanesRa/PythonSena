from Aprendiz import *                                                  # Importa todo de la clase 'aprendiz'
from Curso import *                                                     # Importa todo de la clase 'curso'

with open('herencia/aprendices.txt','r') as flujo:                      # Abre el archivo que se encuentra en la ruta entre paréntesis, despues tiene el parámetro 'r' que es para denotar la lectura del archivo. A esto le da el nombre de 'flujo'
    datos=flujo.read()                                                  # A flujo, que basicamente es todo el archivo de texto, le pasa el método de read que es lectura y se lo asigna a la variable datos
    print(datos)                                                        # Imprime la varaible datos que contiene todo el archivo de texto
    #flujo.write('2560664,maria,123')                                   # Ejemplo comentado de escribir en el archivo una cadena constante
aprendices=[]                                                           # Declaración de la varaible 'aprendices' como una lista vacía
with open('herencia/aprendices.txt','r') as flujo:                      # Abre el archivo que se encuentra en la ruta entre paréntesis, despues tiene el parámetro 'r' que es para denotar la lectura del archivo. A esto le da el nombre de 'flujo'
    for linea in flujo:                                                 # Inicia un ciclo for donde linea va a recorrer flujo, basicamente cada linea del archivo txt
        #print(linea)                                                   # Comentario de impresion de linea, donde imprimía cada linea del archivo que se iba recorriendo
        aprendices.append(linea.rsplit())                               # A la lista aprendices se le inserta la linea que va  a ir recorriendo el for, esto añadido el metodo de rsplit, que quita el salto de linea que tenia al final cada linea

datosxlinea=[]                                                          # Declaración de la varaible 'datosxlinea' como una lista vacía
for aprendiz in aprendices:                                             # Inicia un ciclo for donde 'aprendiz' va a recorrer la lista 'aprendices'
    datosxlinea.append(aprendiz[0].split(','))                          # Inserta a la lista 'datosxlinea' los valores de aprendiz que están van a ser separados por el metodo split por el especificador de ',', ya que actualmente las listas que se encuentran dentro tiene un dato que que es una cadena

#print(ob.getNombre())                                                  # Impresión una instanciacion que no existe jaja, llamando el metodo de 'getNombre'

print(datosxlinea)                                                      # Impresión de la lista datos por línea

listaDeObjetos=[]                                                       # Declaración de la varaible 'listaDeObjetos' como una lista vacía
for apr in datosxlinea:                                                 # Inicia un ciclo for donde 'apr' va a recorrer la lista 'datosxlinea'
     f=apr[0]                                                           # A la variable 'f' se le asigna el valor de 'apr' de 'datosxlinea' en la posicion 0
     n=apr[1]                                                           # A la variable 'n' se le asigna el valor de 'apr' de 'datosxlinea' en la posicion 1
     d=apr[2]                                                           # A la variable 'd' se le asigna el valor de 'apr' de 'datosxlinea' en la posicion 2
     ob=Aprendiz(f,n,d)                                                 # Se instancia un objeto aprendiz con los valores almacenados en las variables(f, n y d)
     print(ob)                                                          # Impresión del objeto creado en la linea anterior                        
     listaDeObjetos.append(ob)                                          # A la lista 'listaDeObjetos' se le inserta el objeto creado en la linea 27

for xx in listaDeObjetos:                                               # Ciclo for en el que xx recorre la lista 'listaDeObjetos'
    print(xx.getNombre())                                               # Impresión del metodo getNombre respecto a xx
    print(xx.getDocumento())                                            # Impresión del metodo getDocumento respecto a xx
    print(xx.getFicha())                                                # Impresión del metodo getFicha respecto a xx