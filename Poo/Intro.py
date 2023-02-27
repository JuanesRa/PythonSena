class Persona: #Creación clase persona
    def __init__(self, nombre, documento): #Creación de la función constructor cuyo nombre es '__init__', que toma como parametro la palabra reservada que es 'self', y el parametro 'nombre'
       self.__nombre = nombre #Asignación del parametro nombre al atributo nombre de la clase persona
       self.__documento = documento
        
    def getNombre(self): #Creacion de la funcion GetNombre, que toma de parametro 'self'
        return self.__nombre #Retorna el valor '__nombre' de la instancia de la clase 'Persona' 
    
    def setNombre(self, nombre): #Creacion de la funcion SetNombre, que toma de parametro 'self'
        self.__nombre = nombre #La instancia '__nombre' de la clase Persona se le asigna el valor que se le da al parámetro 'nombre'
        
    def getDocumento(self):
        return self.__documento
    
    def setDocumento(self, documento):
        self.__documento = documento
        
        
        
#Las siguientes lineas se comentaron ya que las impresiones se traen ahora con el método 'mostrarDatos'


#ob = Persona('Juan',1001094840) #Instanciación de la clase 'Persona', cuyo Parámetro es en este caso una cadena 'Juan'. Recordando que se pasa por parámetro ya que en el constructor requiere el parámetro 'nombre'

#print(objeto.nombre) ### Impresion que se comentó ya que al momento de poner privado el atributo nombre en el constructor dejó de funcionar
#print(ob.getNombre()) #Imprime el método 'getNombre' respecto al objeto
#ob.setNombre('Esteban') #Mediante el método 'setNombre' Setea como nombre 'Esteban' que este a su vez es el parámetro 'nombre' que se solicita en la creación de la función 'setNombre' 
#print(ob.getNombre()) #Imprime el método 'getNombre' ahora con la modificación realizada en el Set

#print(ob.getDocumento()) #Imprime el método 'getDocumento' respecto al objeto
#ob.setDocumento(1001094850) #Mediante el método 'setDocumento' Setea como documento '1001094850' que este a su vez es el parámetro 'documento' que se solicita en la creación de la función 'setDocumento' 
#print(ob.getDocumento()) #Imprime el método 'getDocumento' ahora con la modificación realizada en el Set


class Aprendiz(Persona):
    def __init__(self,nombre,documento,ficha):
        super().__init__(nombre,documento)
        self.__ficha = ficha

    def getFicha(self):
        return self.__ficha

    def mostrarDatos(self):
        print('     \nDATOS APRENDIZ\n')
        print('Nombre:', self.getNombre())
        print('Documento:', self.getDocumento())
        print('Ficha:', self.getFicha())
    
App = Aprendiz('Juan', 1001094840, 2560664)
App.mostrarDatos()


#Metodo get y set para documento Persona /// Linea 12 a 16
#Metodo para ver todos los datos de aprendiz /// Linea 43 a 49