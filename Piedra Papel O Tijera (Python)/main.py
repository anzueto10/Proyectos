#Declaramos la clase jugador para los jugadores
class Jugador():
    def __init__(self):
        self.objeto = ""
        self.ganador = False
        
    def elegir_objeto(self):
        while True:
            print("Escoge tu objeto")
            objeto = input("1. Piedra,  2. Papel,  3. Tijeras: ")
            if objeto == "1":
                self.objeto = "Piedra"
                break
            elif objeto == "2":
                self.objeto = "Papel"
                break
            elif objeto == "3":
                self.objeto = "Tijeras"
                break
            else:
                print("Por favor selecciona una opción válida")
           
#Declaramos la clase juego     
class Juego():
    def __init__(self,nombre):
        self.nombre =  nombre
        self.empate = False
    def terminar_juego(self): pass
    
    def mostrar_resultados(self): 
        if self.empate == False:
            if jugador_1.ganador == True: print(f"El ganador es: Jugador1 y, el perdedor es: Jugador2")
            else: print(f"El ganador es: Jugador2 y, el perdedor es: Jugador1")

    
    #Acá comparaños los objetos si piedra y así
    def comparar_objetos(self,jugador_1,jugador_2):
        if jugador_1.objeto == "Piedra" and jugador_2.objeto == "Papel":
            jugador_1.ganador = False
            jugador_2.ganador = True
        
        elif jugador_1.objeto == "Papel" and jugador_2.objeto == "Tijeras":
            jugador_1.ganador = False
            jugador_2.ganador = True
        
        elif jugador_1.objeto == "Tijeras" and jugador_2.objeto == "Piedra":
            jugador_1.ganador = False
            jugador_2.ganador = True
        
        elif jugador_1.objeto == "Piedra" and jugador_2.objeto == "Tijeras":
            jugador_1.ganador = True
            jugador_2.ganador = False
            
        elif jugador_1.objeto == "Tijeras" and jugador_2.objeto == "Papel":
            jugador_1.ganador = True
            jugador_2.ganador = False
        
        elif jugador_1.objeto == "Papel" and jugador_2.objeto == "Piedra":
            jugador_1.ganador = True
            jugador_2.ganador = False
        elif jugador_1.objeto == jugador_2.objeto:
            print("Es un empate")
            self.empate = True


#Intanciamos
juego_nuevo = Juego("Juego")

jugador_1 = Jugador()
jugador_2 = Jugador()
    
#Elegimos qué eligen
jugador_1.elegir_objeto()
jugador_2.elegir_objeto()

#Comparamos y mostramos ganador
juego_nuevo.comparar_objetos(jugador_1,jugador_2)
juego_nuevo.mostrar_resultados()