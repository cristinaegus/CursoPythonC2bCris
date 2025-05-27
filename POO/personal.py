import datetime

class Persona:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = []
        self.sueldo_hora = sueldo_hora
        self.bono_transporte = 0

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())
        self.bono_transporte += 1

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    def calcula_trabajo(self):
        tiempo_inicial = datetime.timedelta(0)
        entradas = self.fichajes[::2]
        salidas = self.fichajes[1::2]
        tiempo_trabajado = sum([salida - entrada for entrada, salida in zip(entradas, salidas)], start=tiempo_inicial)
        print(f"Tiempo trabajado: {tiempo_trabajado}")
        return tiempo_trabajado
    
    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.sueldo_hora
       
        sueldo = self.bonus
        print(f"Sueldo: {sueldo}")
        return sueldo

import time
if __name__ == "__main__":
    director = Persona('Juan', 'Pérez', 'López')
    secretario = Persona('Juanito', 'Pérez', 'García')

    director.ficha()
    time.sleep(2)
    director.ficha()
    print(director.fichajes)
    #print(director.calcula_trabajo())
    print(director.calcula_sueldo())


class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

def personal(empleado):
    # Aquí puedes acceder a los atributos o métodos del objeto empleado directamente
    print(f"Empleado: {empleado.nombre}, Cargo: {empleado.cargo}")

def empleado_directivo(nombre):
    return Empleado(nombre, "Directivo")
print(empleado_directivo("Juan").cargo)

def empleado_oficinista(nombre):
    return Empleado(nombre, "Oficinista")
print(empleado_oficinista("Ana").cargo)

def empleado_peon(nombre):
    return Empleado(nombre, "Peón")
print(empleado_peon("Luis").cargo)

# El directivo, tiene coche de empresa, y métodos asociados a él.
# El oficinista tiene bonuses
# El peón tiene guardias... etc
class Directivo(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Directivo")
        self.coche_empresa = True

    def asignar_coche(self):
        print(f"{self.nombre} tiene coche de empresa.")    

class Oficinista(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Oficinista")
        self.bonus = 0

    def asignar_bonus(self, cantidad):
        self.bonus += cantidad
        print(f"{self.nombre} ha recibido un bonus de {cantidad}. Total bonus: {self.bonus}")

class Peon(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Peón")
        self.guardias = 0

    def asignar_guardias(self, cantidad):
        self.guardias += cantidad
        print(f"{self.nombre} ha recibido {cantidad} guardias. Total guardias: {self.guardias}")

personal(empleado_directivo("Juan"))
personal(empleado_oficinista("Ana"))
personal(empleado_peon("Luis"))
# Creando instancias de las clases heredadas
juan_directivo = Directivo("Juan")
ana_oficinista = Oficinista("Ana")
luis_peon = Peon("Luis")
juan_directivo.asignar_coche()
ana_oficinista.asignar_bonus(500)
luis_peon.asignar_guardias(5)

# Verificando las instancias
print(isinstance(juan_directivo, Directivo))  # True
print(isinstance(ana_oficinista, Oficinista))  # True
print(isinstance(luis_peon, Peon))  # True
