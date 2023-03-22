from OscarsWinners import *
import csv
WinnersList = []
with open('D:\Python\Archivos\Ejercicio\OscarsMen.csv') as FlujoOscar:

    lectorCSV = csv.reader(FlujoOscar)    
    for row in lectorCSV:
        ow = OscarsWinners(row[0],row[1],row[2],row[3],row[4])
        WinnersList.append(ow)
#print(WinnersList)


with open('D:\Python\Archivos\Ejercicio\OscarsWomen.csv') as FlujoOscar:

    lectorCSV = csv.reader(FlujoOscar)    
    for row in lectorCSV:
        ow = OscarsWinners(row[0],row[1],row[2],row[3],row[4])
        WinnersList.append(ow)
#print(WinnersList)

    # for winner in WinnersList:
    #     print('Index:' + winner.getIndex() + ' Ganador:' + winner.getName() + ' Película:' + winner.getMovie() + ' Año:' + winner.getYear())

def searchActor(nombre, lista_ganadores):
    ganadores_filtrados = []
    for ganador in lista_ganadores:
        if ganador.getName() == nombre:
            ganadores_filtrados.append(ganador)
    return ganadores_filtrados

searchActor("Leonardo DiCaprio", WinnersList)
