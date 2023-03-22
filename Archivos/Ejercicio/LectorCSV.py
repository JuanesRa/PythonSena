import csv
with open('D:\Python\Archivos\Ejercicio\OscarsMen.csv') as FlujoOscar:
    FlujoOscar=csv.reader(FlujoOscar)
    for row in FlujoOscar:
        #print(row)
        print('Index:',row[0])
        print('Year:',row[1])
        print('Age:',row[2])
        print('Name:',row[3])
        print('Movie:',row[3])