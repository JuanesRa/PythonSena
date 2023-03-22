"""

CLASE PADRE "MATERIAL"

"""

class Material:
    def __init__(self, titulo, tipo, autor):
        self.__tituloMaterial = titulo
        self.tipoMaterial = tipo
        self.autorMaterial = autor

    def getTitulo(self):
        return self.__tituloMaterial
    
    def setTitulo(self,titulo):
        self.__tituloMaterial=titulo

    def getTipo(self):
        return self.tipoMaterial
    
    
    def setTipo(self,tipo):
        self.tipoMaterial=tipo

    def getAutor(self): 
        return self.autorMaterial
    
    def setAutor(self,autor):
        self.autorMaterial= autor

"""

CLASE HIJA "LIBRO" DE LA CLASE "MATERIAL"

"""

class Libro(Material):
    def __init__(self, titulo, tipo, autor, editorial):
        Material.__init__(self,titulo,tipo,autor)
        self.editorial = editorial

    def getEditorial(self):
        return self.editorial
    
    def setEditorial(self,editorial):
        self.editorial = editorial

    def getInfoLibro(self):
        print('     \nDATOS LIBRO\n')
        print('Nombre:', self.getTitulo())
        print('Dirección:', self.getTipo())
        print('Teléfono:', self.getAutor())
        print('Código:', self.getEditorial())

"""

CLASE HIJA "Revista" DE LA CLASE "MATERIAL"

"""

class Revista(Material):
    def __init__(self, titulo, tipo, autor, edicion):
        Material.__init__(self,titulo,tipo,autor)
        self.edicion = edicion

    def getEdicion(self):
        return self.edicion

    def setEdicion(self, edicion):
        self.edicion = edicion

    def getInfoRevista(self):
        print('     \nDATOS REVISTA\n')
        print('Nombre:', self.getTitulo())
        print('Dirección:', self.getTipo())
        print('Teléfono:', self.getAutor())
        print('Código:', self.getEdicion())

"""

CLASE PADRE "LECTOR"

"""

class Lector:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono


    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telefono):
        self.__telefono = telefono

"""

CLASE HIJA "Estudiante" DE LA CLASE "LECTOR"

"""

class Estudiante(Lector):
    def __init__(self, nombre, direccion, telefono, codigoEstudiante):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigoEstudiante = codigoEstudiante

    def getCodigoEstudiante(self):
        return self.__codigoEstudiante
    
    def setCodigoEstudiante(self, codigoEstudiante):
        self.__codigoEstudiante = codigoEstudiante

    def mostrarDatosEstudiante(self):
        print('     \nDATOS ESTUDIANTE\n')
        print('Nombre:', self.getNombre())
        print('Dirección:', self.getDireccion())
        print('Teléfono:', self.getTelefono())
        print('Código:', self.getCodigoEstudiante())
"""

CLASE HIJA "Docente" DE LA CLASE "LECTOR"

"""

class Docente(Lector):
    def __init__(self, nombre, direccion, telefono, codigoDocente):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigoDocente = codigoDocente

    def getCodigoDocente(self):
        return self.__codigoDocente
    
    def setCodigoDocente(self, codigoDocente):
        self.__codigoDocente = codigoDocente
    
    def mostrarDatosDocente(self):
        print('     \nDATOS DOCENTE\n')
        print('Nombre:', self.getNombre())
        print('Dirección:', self.getDireccion())
        print('Teléfono:', self.getTelefono())
        print('Código:', self.getCodigoDocente())


"""

CLASE "BIBLIOTECARIO"

"""

class Bibliotecario():
    def __init__(self, idPersonal):
        self.__idPersonal = idPersonal
    
    def getIdPersonal(self):
        return self.__idPersonal 

"""

CLASE "PEDIDO"

"""

class Pedido():
    def __init__(self,idUsuario, material, bibliotecario):
        self.pedido = []
        self.__idUsuario = idUsuario
        self.Material = material
        self.Bibliotecario = bibliotecario
        self.__materiales = []
    
    def getIdUsuario(self):
        return self.__idUsuario
    
    def getTituloMaterial(self):
        return self.Material
    
    
    def getBibliotecario(self):
        return self.Bibliotecario
    
        # Métodos reserva

    def reservar(self, material):
        self.__materiales.append(material)

    def getReservas(self):
        titulos = ""
        for material in self.__materiales:
            return material.getTitulo()
    
    def mostrarDatosPedido(self):
        print('     \nDATOS PEDIDO\n')
        print('Usuario:', self.getIdUsuario())
        print('Material:', self.getTituloMaterial())
        print('Bibliotecario:', self.getBibliotecario())

"""

INSTANCIACIÓN DE OBJETOS Y LLAMADO DE LOS MÉTODOS

"""
idBibli = int(input('Bicliotecario, ingrese su ID de personal\n'))
bibli = Bibliotecario(idBibli)


def Menú():
    print ("\nMENÚ DE OPCIONES\n")
    print ("\t1 - Reservar material ")
    print ("\t2 - Entregar material ")
    print ("\t0 - Salir ")



while True:
    Menú()
    
    opcion = int(input("Seleccione una opción"))
    
    match opcion:
        
        case 1:
            
            print ("\nSELECCIONE QUE TIPO DE LECTOR ES\n")
            print ("\t1 - Estudiante ")
            print ("\t2 - Docente ")
            print ("\t0 - Salir ")
            
            opcion = int(input('Seleccione una opción'))
            
            match opcion:
                
                case 1:
                    nombre = input('Ingrese el nombre del estudiante\n')
                    direccion = input('Ingrese la dirección del estudiante\n')
                    telefono = int(input('Ingrese el teléfono del estudiante\n'))
                    codigoEstudiante = int(input('Ingrese el código del estudiante\n'))
                    
                    aprendiz = Estudiante(nombre, direccion, telefono, codigoEstudiante)
                    
                    
                    print ("\nSELECCIONE QUE TIPO DE MATERIAL VA A RESERVAR\n")
                    print ("\t1 - Libro")
                    print ("\t2 - Revista")
                    print ("\t0 - Salir")
                    
                    opcion = int(input('Seleccione una opción'))
                    
                    match opcion:
                        
                        case 1:
                            
                            titulo = input('Ingrese el nombre del libro')
                            tipo = input('Ingrese el tipo de libro')
                            autor = input('Ingrese el autor del libro')
                            editorial = input('Ingrese la editorial del libro')
                            
                            libro = Libro(titulo, tipo, autor, editorial)

                            aprendiz.mostrarDatosEstudiante()
                            libro.getInfoLibro()

                        case 2:

                            titulo = input('Ingrese el nombre de la revista')
                            tipo = input('Ingrese el tipo de revista')
                            autor = input('Ingrese el autor de la revista')
                            edicion = input('Ingrese la edición de la revista')
                            
                            revista = Revista(titulo, tipo, autor, edicion)   

                            aprendiz.mostrarDatosEstudiante()
                            revista.getInfoRevista()
                    
                case 2:
                    nombre = input('Ingrese el nombre del docente\n')
                    direccion = input('Ingrese la dirección del docente\n')
                    telefono = int(input('Ingrese el teléfono del docente\n'))
                    codigoDocente = int(input('Ingrese el código de docente\n'))
                    
                    docente = Docente(nombre, direccion, telefono, codigoDocente)
                    
                    
                    print ("\nSELECCIONE QUE TIPO DE MATERIAL VA A RESERVAR\n")
                    print ("\t1 - Libro")
                    print ("\t2 - Revista")
                    print ("\t0 - Salir")
                    
                    opcion = int(input('Seleccione una opción'))
                    
                    match opcion:
                        
                        case 1:
                            
                            titulo = input('Ingrese el nombre del libro')
                            tipo = input('Ingrese el tipo de libro')
                            autor = input('Ingrese el autor del libro')
                            editorial = input('Ingrese la editorial del libro')
                            
                            libro = Libro(titulo, tipo, autor, editorial)

                            docente.mostrarDatosDocente()
                            libro.getInfoLibro()

                        case 2:

                            titulo = input('Ingrese el nombre de la revista')
                            tipo = input('Ingrese el tipo de revista')
                            autor = input('Ingrese el autor de la revista')
                            edicion = input('Ingrese la edición de la revista')
                            
                            revista = Revista(titulo, tipo, autor, edicion)   

                            docente.mostrarDatosDocente()
                            revista.getInfoRevista()
                case 3:
                    break
            
        case 2:
            break
        case 0:
            break
        
        
# lectura = Libro('Veinte mil leguas de viaje submarino','Ciencia Ficción','Julio Verne','Alianza Editorial')
# lectura2 = Revista('Materia y energía oscuras','Científica', 'Annia Domènech', 'Global Astronomía')


# #aprendiz = Estudiante('Juan','Cra 38', 3126486145,2560664)
# #profesor = Docente('Esteban','Cra 10', 3167846163,2560665)

# bibli = Bibliotecario(12345)

# pedido = Pedido(aprendiz.getCodigoEstudiante(),lectura.getTitulo(),bibli.getIdPersonal())

# pedido.reservar(lectura)    
# pedido.reservar(lectura2)



# pedido.mostrarDatosPedido()



#aprendiz.mostrarDatosEstudiante()
#profesor.mostrarDatosDocente()
