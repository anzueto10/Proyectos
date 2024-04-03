import random
cuentas = []
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = self.crear_numero_de_cuenta_bancaria()

    def crear_numero_de_cuenta_bancaria(self):
        num_cuenta = ''.join(str(random.randint(0, 9)) for _ in range(5))
        return num_cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado con éxito.")
        else:
            print("El depósito tiene que ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado con éxito.")
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def mostrar_datos(self):
        print(f"""
----Cuenta de banco {self.numero_cuenta}-----
    
    Propietario: {self.titular}
    Saldo actual: {self.saldo}
    Numero de cuenta: {self.numero_cuenta}
    
--------------------------------
              """)


def obtener_cantidad():
    while True:
        try: 
            monto = float(input("Ingrese la cantidad: "))
            if monto <= 0: print("La cantidad debe ser mayor que cero.")
            else: return monto
        except ValueError: print("Ingrese una cantidad válida.")
        
def obtener_nombre():
    titular = input("Ingrese su nombre: ")
    return titular

def agregar_a_la_lista_de_cuentas(cuenta):
    cuentas.append(cuenta)
    
def crear_cuenta():
    nuva_cuenta = CuentaBancaria(obtener_nombre())
    agregar_a_la_lista_de_cuentas(nuva_cuenta)
    print("Cuenta creada")
    
def mostrar_cuentas():
    while True: 
        try: 
            cuentas_existentes = "\n".join([f"{i+1}. {cuenta.numero_cuenta}. {cuenta.titular}" for i, cuenta in enumerate(cuentas)])
            cuenta_a_manejar = int(input(f"""
--------------- Seleccione la cuenta ------------------
{cuentas_existentes}
------------------------------------------------------:
""")) -1
        
            cuenta_a_manejar = cuentas[cuenta_a_manejar]
            return cuenta_a_manejar
        except:
            print("Ingrese una cuenta válida")

def verificar_si_hay_cuenta():
    if len(cuentas) > 0: return True
    else: return False
                
def iniciar_programa():
    
    while True:

        accion = input("""
    --------------- Qué desea hacer ------------------
    1. Hacer un depósito
    2. Hacer un retiro
    3. Mostrar datos de la cuenta
    4. Crear una cuenta
    5. Salir
                           :""")
        if verificar_si_hay_cuenta(): 
            if accion == "1":
                cuenta = mostrar_cuentas()
                cantidad = obtener_cantidad()
                cuenta.depositar(cantidad)
            elif accion == "2":
                cuenta = mostrar_cuentas()
                cantidad = obtener_cantidad()
                cuenta.retirar(cantidad)
            elif accion == "3":
                cuenta = mostrar_cuentas()
                cuenta.mostrar_datos()
            elif accion == "4":
                crear_cuenta()
            elif accion == "5":
                break
            else:
                print("Opción inválida. Por favor, elija una opción válida.")
        elif accion == "4": crear_cuenta()
        elif accion == "5": break
        elif not verificar_si_hay_cuenta(): print("Por favor, cree una cuenta antes de hacer trámites")
        

iniciar_programa()
