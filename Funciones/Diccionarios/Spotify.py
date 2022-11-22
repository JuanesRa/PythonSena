playlist = {}

def buscarCancion(playlist):
    cancion = input('Ingrese el nombre de la canción que desea buscar')
    for i in playlist.keys():
        if cancion == i:
            print(cancion, 'se encuentra en su playlist y cuenta con una duración de',playlist[i]['duracion'])
            return None
        else:
            print(cancion,'no se encuentra en su playlist, puede añadirla en el menú de opciones')
    
def buscarArtista(playlist):
    artista = input('Ingrese el nombre del artista que desea buscar')
    for i in (playlist.values()):
        if i['artista'] == artista:
            print(artista, 'se encuentra en su playlist')
            return None
        else:
            print(artista, 'No se encuentra en su playlist')
    
def agregarCancion(playlist):
    cancion = input('Ingrese el nombre de la canción que va a agregar')
    playlist.update({cancion:{}})
    return playlist

def agregarDatosCancion(playlist):
    cancion = input('Ingrese el nombre de la cancion a la cual le va a agregar la información')
    if cancion in playlist:
        artista = input('Ingrese el nombre del artista')
        duracion = input('Ingrese la duración de la canción(El formato a utilizar es: mm:ss)')
        genero = input('Ingrese el género de la canción')
        playlist.update({cancion:{'artista':artista,'genero':genero,'duracion':duracion}})
        return playlist
    else:
        print('La canción no está en la playlist')


def eliminarArtista(playlist):
    eliminar = input('Ingrese el nombre de la canción que desea eliminar')
    for i in playlist.keys():
        if eliminar == i:
            del playlist[i]
            print(eliminar, 'fue eliminada de su playlist')
            return None
        else:
            print('La canción no fue encontrada')
    
def cancionMasLarga(playlist):
    largest = dict
    largestValue = 0
    for i in playlist.keys():
        minutos = playlist[i]['duracion'][0]
        minutos += playlist[i]['duracion'][1]
        segundos = playlist[i]['duracion'][3]
        segundos += playlist[i]['duracion'][4]
        total = int(minutos) + int(segundos)*60
        if largestValue <= total:
            largestValue = total
            largest = i
    print('La canción más larga de la playlist es',largest)
    
def cancionMasCorta(playlist):
    shortest = dict
    shortestValue = 999999
    for i in playlist.keys():
        minutos = playlist[i]['duracion'][0]
        minutos += playlist[i]['duracion'][1]
        segundos = playlist[i]['duracion'][3]
        segundos += playlist[i]['duracion'][4]
        total = int(minutos) + int(segundos)*60
        if shortestValue >= total:
            shortestValue = total
            shortest = i
    print('La canción más corta de la playlist es',shortest)
    

def Menú():
    print ("Menú de opciones")
    print ("\t1 - Buscar una canción")
    print ("\t2 - Buscar un artista")
    print ("\t3 - Agregar una cancion")
    print ("\t4 - Agregar datos de una cancion")
    print ("\t5 - Eliminar un artista")
    print ("\t6 - Mostrar canciones de la playlist ordenada")
    print ("\t7 - Mostrar canción más larga")
    print ("\t8 - Mostrar canción más corta")
    print ("\n\t0 - Salir")



while True:
    Menú()
    
    opcion = int(input("Seleccione una opción"))
    
    match opcion:
        case 1:
            buscarCancion(playlist)
        case 2:
            buscarArtista(playlist)
        case 3:
            agregarCancion(playlist)
        case 4:
            agregarDatosCancion(playlist)
        case 5:
            eliminarArtista(playlist)
        case 6:
            print(sorted(playlist))
        case 7:
            cancionMasLarga(playlist)
        case 8:
            cancionMasCorta(playlist)
        case 0:
            break