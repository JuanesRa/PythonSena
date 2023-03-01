class Producto:
    
    __cont = 0
    __total = 0
    
    def __init__(self,nombre,precio):
        self.__nombre = nombre
        self.__precio = precio
        Producto.__cont += 1
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self,precio):
        self.__precio = precio
        
    def calcularIva(self):
        iva = self.__precio * 0.19
        total = self.__precio + iva
        Producto.__total += total
        return total
        
    def cantidadCarrito():
        return Producto.__cont
    
    def totalCarrito():
        return Producto.__total
    


print('\nCARRITO DE COMPRAS')

        
producto = Producto('Televisor',2200000)
producto2 = Producto('Celular',1500000)
producto3 = Producto('Computador portátil',3800000)



print('\nProducto:',producto.getNombre())
print('Precio:',producto.getPrecio())
print('Producto con IVA:',producto.calcularIva())

print('\nProducto:',producto2.getNombre())
print('Precio:',producto2.getPrecio())
print('Producto con IVA:',producto2.calcularIva())

print('\nProducto:',producto3.getNombre())
print('Precio:',producto3.getPrecio())
print('Producto con IVA:',producto3.calcularIva())

print('\nEl total de productos en el carrito de compras es:',Producto.cantidadCarrito())
print('\nEl total del carrito de compras es:',Producto.totalCarrito())