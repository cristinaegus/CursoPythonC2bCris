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

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())

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
    secretario.ficha()