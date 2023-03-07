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

"""

CLASE PADRE "LECTOR"

"""

class Lector:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__materiales = []

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

# Métodos reserva

    def reservar(self, material):
        self.__materiales.append(material)

    def getReservas(self):
        titulos = ""
        for material in self.__materiales:
            return material.getTitulo()


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
    
    def getIdUsuario(self):
        return self.__idUsuario
    
    def getTituloMaterial(self):
        return self.Material
    
    
    def getBibliotecario(self):
        return self.Bibliotecario
    
    def mostrarDatosPedido(self):
        print('     \nDATOS PEDIDO\n')
        print('Usuario:', self.getIdUsuario())
        print('Material:', self.getTituloMaterial())
        print('Bibliotecario:', self.getBibliotecario())

"""

INSTANCIACIÓN DE OBJETOS Y LLAMADO DE LOS MÉTODOS

"""

lectura = Libro('Veinte mil leguas de viaje submarino','Ciencia Ficción','Julio Verne','Alianza Editorial')
lectura2 = Revista('Materia y energía oscuras','Científica', 'Annia Domènech', 'Global Astronomía')


aprendiz = Estudiante('Juan','Cra 38', 3126486145,2560664)
#profesor = Docente('Esteban','Cra 10', 3167846163,2560665)

bibli = Bibliotecario(12345)

aprendiz.reservar(lectura)
aprendiz.reservar(lectura2)



pedido = Pedido(aprendiz.getCodigoEstudiante(),lectura.getTitulo(),bibli.getIdPersonal())

pedido.mostrarDatosPedido()



#aprendiz.mostrarDatosEstudiante()
#profesor.mostrarDatosDocente()