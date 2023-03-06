"""

CLASE MATERIAL

"""

class Material:
    def __init__(self,tituloMaterial,tipoMaterial,autor):
        self.__tituloMaterial = tituloMaterial
        self.tipoMaterial = tipoMaterial
        self.autor = autor
        
    def getTituloLibro(self):
        return self.__tituloMaterial
    
    def getTituloLibro(self):
        return self.tipoMaterial
    
    def getAutor(self):
        return self.autor
        
    def reservarFecha(self):
        pass
    
    def entregarFecha(self):
        pass

"""

SUBCLASE LIBRO DE LA CLASE MATERIAL

"""  
        
class Libro(Material):
    def __init__(self, tituloLibro, tipoLibro, autor,editorial):
        Material.__init__(self,tituloLibro, tipoLibro,autor)
        self.editorial = editorial

    
    def reservarFecha(self):
        pass
    def entregarFecha(self):
        pass
    
"""

SUBCLASE REVISTA DE LA CLASE MATERIAL

"""

class Revista(Material):
    def __init__(self, tituloRevista, tipoRevista, autor,edicion):
        Material.__init__(self,tituloRevista, tipoRevista,autor)
        self.edicion = edicion
    
    def reservarFecha(self):
        pass
    def entregarFecha(self):
        pass

lectura = Libro('Veinte mil leguas de viaje submarino','Novela - Ciencia Ficción','Julio Verne','Alianza Editorial')


"""

CLASE LECTOR

"""


class Lector:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        
        
    def getNombreLector(self):
        return self.__nombre
    
    def getDireccionLector(self):
        return self.__direccion
    
    def getTelefonoLector(self):
        return self.__telefono
    
    def reservar_material(self, material):
        pass
    
    def entregar_material(self, material):
        pass


"""

SUBCLASE ESTUDIANTE DE LA CLASE LECTOR

"""

class Estudiante(Lector):
    def __init__(self, nombre, direccion, telefono, codigoEstudiante):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigoEstudiante = codigoEstudiante
        
    def getCodigoEstudiante(self):
        return self.__codigoEstudiante
        
    def mostrarDatosEstudiante(self):
        print('     \nDATOS ESTUDIANTE\n')
        print('Nombre:', self.getNombreLector())
        print('Dirección:', self.getDireccionLector())
        print('Teléfono:', self.getTelefonoLector())
        print('Código:', self.getCodigoEstudiante())
        
    
    def reservar_libro(self, libro):
        pass
    
    def entregar_libro(self, libro):
        pass


"""

SUBCLASE DOCENTE DE LA CLASE LECTOR

"""

class Docente(Lector):
    def __init__(self, nombre, direccion, telefono, codigoDocente):
        Lector.__init__(self, nombre, direccion, telefono)
        self.__codigoDocente = codigoDocente
        
    def getCodigoDocente(self):
        return self.__codigoDocente
    
    def mostrarDatosEstudiante(self):
        print('     \nDATOS DOCENTE\n')
        print('Nombre:', self.getNombreLector())
        print('Dirección:', self.getDireccionLector())
        print('Teléfono:', self.getTelefonoLector())
        print('Código:', self.getCodigoDocente())
    
    def reservar_libro(self, libro):
        pass
    
    def entregar_libro(self, libro):
        pass
        
        
"""

INSTANCIACIÓN Y LLAMADO DE LOS MÉTODOS

"""
        
aprendiz = Estudiante('Juan','Cra 38', 3126486145,2560664)
profesor = Docente('Esteban','Cra 10', 3167846163,2560665)
aprendiz.mostrarDatosEstudiante()
profesor.mostrarDatosEstudiante()
