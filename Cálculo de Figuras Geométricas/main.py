from abc import ABC, abstractmethod
import math

#Definir las clases (con abs)
class Figura(ABC):
    @abstractmethod
    def __init__(self, color):
        self.color = color
    
    #Definimos los métodos abstractos    
    @abstractmethod
    def calcular_area(self): pass
    
    @abstractmethod
    def calcular_perimetro(self): pass
    
class Circulo(Figura):
    def __init__(self,color, radio):
        super().__init__(color)
        self.radio = radio
    
    #Metodo para conseguir el area del círculo (Pi x radio al cuadrado)
    def calcular_area(self): return int(math.pi * self.radio**2)
    
    #Método para conseguir el perímetro del círculo (2 por pi por radio)
    def calcular_perimetro(self): return int(2 * math.pi * self.radio)
        
        
class Triangulo(Figura):
    def __init__(self,color,base,altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
    
    #Método para conseguir el area del triángulo
    def calcular_area(self): return self.base * self.altura
    
    def calcular_perimetro(self): return self.base * 3
        
        
class Rectangulo(Figura):
    def __init__(self,color,base,altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
        
    def calcular_area(self): return self.base * self.altura
    
    def calcular_perimetro(self): return self.base * 2 + self.altura *2


#Instanciamos las clases en objetos para que se puedan usar y así
circulo = Circulo("Azul", 20)
triangulo = Triangulo("Amarillo", 40, 40)
rectangulo = Rectangulo("Verde", 200, 50)

#Usamos los métodos para que nos calcule el area y perímetro de las figuras
print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())
print("\n")

print("Área del triángulo:", triangulo.calcular_area())
print("Perímetro del triángulo:", triangulo.calcular_perimetro())
print("\n")

print("Área del rectángulo:", rectangulo.calcular_area())
print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())