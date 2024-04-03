from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    
#Definimos la clase de carrito de compras
class Carrito():
    def __init__(self):
        self.lista = []
        self.precio_final = 0
    
    def agregar_producto(self, producto):
        self.lista.append(producto.nombre)
        self.precio_final = self.precio_final  + int(producto.precio)
        print(f"Se agregó un producto: {producto.nombre}\n")
        
    def quitar_producto(self, producto): 
        self.lista.remove(producto.nombre)
        self.precio_final = self.precio_final - int(producto.precio)
        print(f"Se removió un producto: {producto.nombre}\n")
        
    def vacear_carrito(self): 
        self.lista.clear()
        self.precio_final = 0
        print("Se vació el carrito \n")
        
    def calcular_total(self): print(f"Total: {self.precio_final}")
    
    def mostrar_lista(self): print(f"Lista del carrito: {self.lista}")
    
#Definimmos y heradmos las clases de los productos
#Comida
class Comida(Producto):
    @abstractmethod
    def __init__(self,nombre,precio,stock,calorias,sabor):
        super().__init__(nombre,precio,stock)
        self.calorias = calorias
        self.sabor = sabor
        
    #Métodos y así

class Fruta(Comida): 
    @abstractmethod
    def __init__(self,nombre,precio,stock,calorias,sabor,azucar,semillas):
        super().__init__(nombre,precio,stock,calorias,sabor)
        self.azucar = azucar
        self.semillas = semillas

class Manzana(Fruta):
    def __init__(self,nombre,precio,stock,calorias,sabor,azucar,semillas,color_manzana):
        super().__init__(nombre,precio,stock,calorias,sabor,azucar,semillas)
        self.color_manzana = color_manzana


#Electrónicos---------
class Electronicos(Producto): 
    @abstractmethod
    def __init__(self,nombre,precio,stock,consumo_electrico):
        super().__init__(nombre,precio,stock)
        self.consumo_electrico = consumo_electrico

class Celular(Electronicos):
    @abstractmethod
    def __init__(self,nombre,precio,stock,consumo_electrico, gama):
        super().__init__(nombre,precio,stock,consumo_electrico)
        self.gama = gama
    
class SamsungGalaxyS20(Celular): 
    def __init__(self,nombre,precio,stock,consumo_electrico, gama, dueño):
        super().__init__(nombre,precio,stock,consumo_electrico, gama)
        self.dueño = dueño

#Bebidas------
class Bebida(Producto):
    @abstractmethod
    def __init__(self,nombre,precio,stock,contenido,temperatura):
        super().__init__(nombre,precio,stock)
        self.contenido = contenido
        self.temperatura = temperatura
    
class Gaseosa(Bebida):
    @abstractmethod
    def __init__(self,nombre,precio,stock,contenido,temperatura,azucar_saturada):
        super().__init__(nombre,precio,stock,contenido,temperatura)
        self.azucar_saturada = azucar_saturada

class SevenUp(Gaseosa):
    def __init__(self,nombre,precio,stock,contenido,temperatura,azucar_saturada,presentacion):
        super().__init__(nombre,precio,stock,contenido,temperatura,azucar_saturada)
        self.presentacion = presentacion

carrito = Carrito()
manzanita_verde = Manzana("Manzana1", 15,1000,20,"Bueno","20 gramos","Pocas","Verde")
samsung_galaxy_20 = SamsungGalaxyS20("Samsung_pro",2000,30,"15w", "Alta", "Anzueto")
seven_up = SevenUp("Seven1", 20, 700, "15 litros", "Fría", "Alta", "Seven Limon X")


#Agreagmos el primer producto e imprimos el total
carrito.agregar_producto(manzanita_verde)
carrito.calcular_total()

#Agregamos otro y lo quitamos, luego imprimoso la lista
carrito.agregar_producto(seven_up)
carrito.quitar_producto(seven_up)
carrito.mostrar_lista()

#Imprimimos el total
carrito.calcular_total()

#Agreamos 2 y vaciamos el carrito
carrito.agregar_producto(manzanita_verde)
carrito.agregar_producto(manzanita_verde)
carrito.agregar_producto(seven_up)
carrito.vacear_carrito()
carrito.mostrar_lista()

#Agreamos 3 e imprimos el precio final
carrito.agregar_producto(seven_up)
carrito.agregar_producto(samsung_galaxy_20)
carrito.agregar_producto(manzanita_verde)
carrito.mostrar_lista()
carrito.calcular_total()

