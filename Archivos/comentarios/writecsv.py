import csv                                            # Importación del módulo csv
header=['Fruit','Price']                              # Declaración de la lista 'header' que almacena 'Fruit' y 'Price' dentro de ella
rows=[['Apple',1200],                                 # Declaración de la lista 'rows' que almacena listas dentro de ella
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('archivos/example.csv','w') as csvfile:    # Abre el archivo que se encuentra en la ruta entre paréntesis, despues tiene el parámetro 'w' que es para denotar la escritura del archivo. A esto le da el nombre de 'csvfile'
    csvwriter=csv.writer(csvfile)                     # Crea el objeto 'csvwriter' que se usará para escribir los datos. Se crea a partir de 'csvfile'
    csvwriter.writerow(header)                        # Escribe los encabezados de las columnas usando de parametros los valores de la lista 'header'
    csvwriter.writerows(rows)                        # Escribe las columnas usando de parametros los valores de la lista 'rows'