class Persona: #Creación clase persona
    def __init__(self, nombre, documento): #Creación del constructor cuyo nombre es '__init__', que toma como parametro la palabra reservada que es 'self', y el parametro 'nombre'
       self.__nombre = nombre #Asignación del parametro nombre al atributo nombre de la clase persona
       self.__documento = documento #Asignación del parametro documento al atributo documento de la clase persona
        
    def getNombre(self): #Creacion del método GetNombre, que toma de parámetro 'self'
        return self.__nombre #Retorna el valor '__nombre' de la instancia de la clase 'Persona' 
    
    def setNombre(self, nombre): #Creacion del método SetNombre, que toma de parámetro 'self'
        self.__nombre = nombre #La instancia '__nombre' de la clase Persona se le asigna el valor que se le da al parámetro 'nombre'
        
    def getDocumento(self): #Creacion del método GetDocumento, que toma de parámetro 'self'
        return self.__documento #Retorna el valor '__documento' de la instancia de la clase 'Persona' 
    
    def setDocumento(self, documento): #Creacion del método SetDocumento, que toma de parámetro 'self'
        self.__documento = documento #La instancia '__documento' de la clase Persona se le asigna el valor que se le da al parámetro 'documento'
        
        
        
#Las siguientes lineas se comentaron ya que las impresiones se traen ahora con el método 'mostrarDatos'


#ob = Persona('Juan',1001094840) #Instanciación de la clase 'Persona', cuyo Parámetro es en este caso una cadena 'Juan'. Recordando que se pasa por parámetro ya que en el constructor requiere el parámetro 'nombre'

#print(objeto.nombre) ### Impresion que se comentó ya que al momento de poner privado el atributo nombre en el constructor dejó de funcionar
#print(ob.getNombre()) #Imprime el método 'getNombre' respecto al objeto
#ob.setNombre('Esteban') #Mediante el método 'setNombre' Setea como nombre 'Esteban' que este a su vez es el parámetro 'nombre' que se solicita en la creación de la función 'setNombre' 
#print(ob.getNombre()) #Imprime el método 'getNombre' ahora con la modificación realizada en el Set

#print(ob.getDocumento()) #Imprime el método 'getDocumento' respecto al objeto
#ob.setDocumento(1001094850) #Mediante el método 'setDocumento' Setea como documento '1001094850' que este a su vez es el parámetro 'documento' que se solicita en la creación de la función 'setDocumento' 
#print(ob.getDocumento()) #Imprime el método 'getDocumento' ahora con la modificación realizada en el Set


class Aprendiz(Persona): #Definicion de la clase 'Aprendiz' que hereda de la clase llamada 'Persona'
    def __init__(self,nombre,documento,ficha): #Constructor de la clase aprendiz que recibe 3 parámetros, (nombre,documento y ficha)
        Persona.__init__(self,nombre,documento) #Llamado al constructor de la clase 'Persona', al que se le pasan los parámetro (nombre y documento)
        self.__ficha = ficha #Inicializacón del atributo '__ficha' el cual es privado

    def getFicha(self): #Creacion del método 'getFicha'
        return self.__ficha #Retorno del valor del atributo '__ficha'

    def mostrarDatos(self): #Creacion del método 'mostrarDatos'
        print('     \nDATOS APRENDIZ\n') #Impresion que una cadena con saltos de línea al inicio y final de la cadena
        print('Nombre:', self.getNombre()) #Impresión del valor de nombre, por medio del método 'getNombre' 
        print('Documento:', self.getDocumento()) #Impresión del valor de documento, por medio del método 'getDocumento'
        print('Ficha:', self.getFicha()) #Impresión del valor de ficha, por medio del método 'getFicha'
    
App = Aprendiz('Juan', 1001094840, 2560664) #Creación de la instancia de la clase aprendiz que se llama 'App', al cual se le pasa un valor de cadena y dos numericos correspondientes a (nombre,documento y ficha)
App.mostrarDatos() #Llamado al método 'mostrarDatos' de la instancia 'App' que imprime los datos de aprendiz


#Metodo get y set para documento Persona /// Linea 12 a 16
#Metodo para ver todos los datos de aprendiz /// Linea 43 a 50