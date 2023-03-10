flujo=open('archivos/comentarios/inicio.txt','a')           # Creación del objeto flujo, al cual se le pasa el método open, de parámetro se le da una ruta, y la 'a' hace referencia a que es la actualización del archivo de texto que anteriormente se creó
#datos=flujo.read()                             # Comentario en el cual se le daba a la variable datos el valor del objetos flujo con el método de leer
#print(datos)                                   # Impresión de la variable datos el cual mostraba el contenido del archivo. (Esto se comentarió en clase debido a que el archivo pasó de ser de lectura a escritura, por lo cual tocaba comentar esta parte para que no produjera error)
flujo.write('\nCuando estudian con juicio')     # Al objeto flujo se le pasa el método de escribir, se le pasa una cadena con un salto de línea al inicio
datos=flujo.read()                              # Comentario en el cual se le daba a la variable datos el valor del objetos flujo con el método de leer
print(datos)                                    # Impresión de la variable datos el cual muestra el contenido del archivo, como es un archivo de escritura, la ejecución de este da error
flujo.close()                                   # Cierre del archivo