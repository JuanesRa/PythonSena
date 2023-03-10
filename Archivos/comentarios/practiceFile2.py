from Aprendiz import *                                                                  # Importa todo de la clase 'aprendiz'
from Curso import *                                                                     # Importa todo de la clase 'curso'

nombre=input('ingrese nombre del aprendiz')                                             # 'nombre' es una variable que almacena un valor por teclado
documento=int(input('ingrese documento del aprendiz'))                                  # 'documento' es una variable que almacena un valor por teclado que se transforma de cadena a entero
ficha=input('ingrese ficha del aprendiz')                                               # 'ficha' es una variable que almacena un valor por teclado

ap=Aprendiz(ficha,nombre,documento)                                                     # Instanciación de 'Aprendiz', y se utiliza de parámetros los valores almacenados en las variables que fueron ingresadas por teclado (ficha,nombre y documento)

nombreCurso=input('ingrese nombre del curso')                                           # 'nombreCurso' es una variable que almacena un valor por teclado
horas=int(input('ingrese intensidad horaria del curso'))                                # 'horas' es una variable que almacena un valor por teclado que se transforma de cadena a entero
c1=Curso(nombreCurso,horas)                                                             # Instanciación de 'Curso', y se utiliza de parámetros los valores almacenados en las variables que fueron ingresadas por teclado (nombrecurso y horas)
ap.agregarCurso(c1)                                                                     # A la instancia de 'Aprendiz' que es 'ap' se le pasa el metodo de 'agregarCurso' y como parámetro se le pasa la instancia de 'Curso' que es 'c1'

with open('herencia/aprendices.txt','a') as flujo:                                      # Abre el archivo que se encuentra en la ruta entre paréntesis, despues tiene el parámetro 'a' que es para que permita la actualización del archivo. A esto le da el nombre de 'flujo'
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')       # A flujo, que basicamente es todo el archivo de texto, le pasa el método de write que es de escritura. Y concatena los metodos getter de la instanciacion de Aprendiz