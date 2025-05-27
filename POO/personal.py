from abc import ABC, abstractmethod
import datetime
import time

# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = []
        self.sueldo_hora = sueldo_hora
        self.bono_transporte = 0

    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

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

    @abstractmethod
    def calcula_sueldo(self):
        pass

# Solo se pueden instanciar las subclases:
class Directivo(Persona):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.coche_empresa = True

    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.sueldo_hora
        sueldo_total = sueldo + self.bono_transporte
        print(f"Sueldo Directivo: {sueldo:.2f} € + Dieta transporte: {self.bono_transporte} € = Total: {sueldo_total:.2f} €")
        return sueldo_total

class Oficinista(Persona):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.bonus = 0

    def asignar_bonus(self, cantidad):
        self.bonus += cantidad
        print(f"{self.nombre} ha recibido un bonus de {cantidad}. Total bonus: {self.bonus}")

    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.sueldo_hora
        sueldo_total = sueldo + self.bono_transporte + self.bonus
        print(f"Sueldo Oficinista: {sueldo:.2f} € + Dieta transporte: {self.bono_transporte} € + Bonus: {self.bonus} € = Total: {sueldo_total:.2f} €")
        return sueldo_total

class Peon(Persona):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.guardias = 0

    def asignar_guardias(self, cantidad):
        self.guardias += cantidad
        print(f"{self.nombre} ha recibido {cantidad} guardias. Total guardias: {self.guardias}")

    def calcula_sueldo(self):
        tiempo_trabajado = self.calcula_trabajo()
        sueldo = tiempo_trabajado.total_seconds() / 3600 * self.sueldo_hora
        sueldo_total = sueldo + self.bono_transporte + (self.guardias * 10)
        print(f"Sueldo Peón: {sueldo:.2f} € + Dieta transporte: {self.bono_transporte} € + Guardias: {self.guardias*10} € = Total: {sueldo_total:.2f} €")
        return sueldo_total

# Ejemplo de uso:
if __name__ == "__main__":
    jefe = Directivo('Ana', 'García', 'López')
    oficinista = Oficinista('Luis', 'Martínez', 'Ruiz')
    peon = Peon('Pedro', 'López', 'Sánchez')

    jefe.ficha()
    time.sleep(1)
    jefe.ficha()
    jefe.calcula_sueldo()

    oficinista.ficha()
    time.sleep(1)
    oficinista.ficha()
    oficinista.asignar_bonus(200)
    oficinista.calcula_sueldo()

    peon.ficha()
    time.sleep(1)
    peon.ficha()
    peon.asignar_guardias(3)
    peon.calcula_sueldo()
