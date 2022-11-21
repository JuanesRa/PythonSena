"""Generar dissionario canciones diccionario duración
Artista
Genero 
Duracion

Buscar por artista 
Cancion
Anexar cancion 
Eliminar artista
Buscar canciones 
Anexar artista
Ordenar alfabeticamente 
El que tiene mas  canciones 
El que tiene  las cancion mas larga 
El que tiene la cancion mas corta """

listareproduccion = {"Ed Sheeran" :(
                            "cancion" "Make it rain", 
                            "duracion" "6:44", 
                            "genero" "Pop"
                            ),
                   "The Weeknd": (
                            "cancion" "Nothing Compares", 
                            "duracion" "3:42" , 
                            "genero" "Pop"
                            ),
                    "Coldplay": (
                                "cancion" "Charlie Brown",
                                "duracion" "4:45",
                                "genero" "Pop"                                                                 
                            ),
                    "Linkin Park": (
                                "cancion" "What I've Done",
                                "duracion"  "3:25",
                                "genero" "rock"
                                ),
                    "Andrés Cepéda": (
                                "cancion" "Embrujo",
                                "duracion" "2:42",
                                "genero" "Tropi pop"
                    )
                    
                    }               

# funcion buscar
def artista (artis, playlist):
    if artis in playlist:
        print(playlist[artis])
        return 1
    else:
        print("El artista no se encuenta")
        return 2

#funcion agregar artitas
def agregarArtista(veri, playlist):
    if veri ==2:
        y=input("Escribe el nombre del artista que quieres agregar\n")
        playlist[y]=()
        print(playlist)
        return 1
#Agregar cancion
def agregarCancion (artis,playlist):
    if x ==1:
        c=input("Nombre de la cancion que quieres agregar:\n")
        g=input("Género de la cancion:\n")
        d=input("duracion de la cancion:\n")
        dici=("cancion", c,"duracion", d,"genero", g)
        playlist[artis]+=dici
        print(playlist)
    else:
        print("Debes agregar el artista primero")

cantante=input ("Escribe el nombre del artita que quieres buscar:\n")

x= artista(cantante,listareproduccion)


#funciones
agregarArtista(x, listareproduccion)
x= artista(cantante,listareproduccion)
artiscan=input("Nombre del artista al que le quieres agregar una cancion:\n")
agregarCancion(artiscan, listareproduccion)
















"""

x=str(input("ingrese el artista:"))
artista(x,listareproduccion)

"""