#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

############
# Herencia #
############
"""
La Herencia permite definir clases con características derivadas de otras que 
no necesitan definirse en las clases herederas. Aunque pueden sobreescribirse.
"""
#----------------------------
# Clase padre (o superclase)
#----------------------------
class Mamifero:
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible

    # Los métodos correr y saltar son heredables por cualquier mamífero
    def correr(self):
        print("Este animal corre")

    def saltar(self):
        print("Este animal salta")
    
    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un mamífero")
        else:
            print("No puedes comerte este animal")    

#---------------------------
# Clases hijo (o subclases)
#---------------------------
class Animal_de_granja(Mamifero):
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible
        self.en_choza = False

    # Hay dos métodos nuevos que permiten modificar un atributo que no existía en la superclase
    # Los heredarán las subclases
    def guardar_en_choza(self):
        self.en_choza = True

    def sacar_de_choza(self):
        self.en_choza = False

    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un animal de granja")
        else:
            print("No puedes comerte este animal")


class Animal_domestico(Animal_de_granja):
    def __init__(self, nombre):
        self.nombre = nombre
        self.patas = 4
        self.cola = True
        self.comestible = False
        self.en_choza = False
        self.en_casa = False

    # Hay dos métodos nuevos que permiten modificar un atributo que no existía en la superclase
    def guardar_en_casa(self):
        self.en_casa = True

    def sacar_de_casa(self):
        self.en_casa = False

    def me_lo_como(self):
        print(f"No te puedes comer a {self.nombre}")
        raise NotImplementedError("Este método no está disponible en la subclase")


ciervo = Mamifero(comestible = True)
ciervo.comestible
ciervo.correr()
# El ciervo no se puede meter en una choza
ciervo.guardar_en_choza()
ciervo.me_lo_como()

raton = Mamifero(comestible = False)
raton.correr()
raton.saltar()
raton.me_lo_como()

cerdo = Animal_de_granja(comestible = True)
cerdo.comestible
cerdo.correr()
cerdo.cola

cerdo.en_choza
cerdo.guardar_en_choza()
cerdo.en_choza
cerdo.sacar_de_choza()
cerdo.en_choza

cerdo.guadar_en_casa()

cerdo.me_lo_como()

burro = Animal_de_granja(comestible = False)
burro.me_lo_como()

perro = Animal_domestico("Lassie")
perro.patas
# Este atributo no tiene un método que lo modifique
perro.comestible
perro.nombre

# Los métodos heredados siguen funcionando
perro.en_choza
perro.guardar_en_choza()
perro.en_choza
perro.sacar_de_choza()
perro.en_choza

perro.correr()
perro.saltar()

# Y además tieme métodos nuevos
perro.en_casa
perro.guardar_en_casa()
perro.en_casa
perro.sacar_de_casa()
perro.en_casa

perro.me_lo_como()


# ____________________________________________________
# Para no tener que reescribir la funcion __init__

class Mamifero:
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible

    # Los métodos correr y saltar son heredables por cualquier mamífero
    def correr(self):
        print("Este animal corre")

    def saltar(self):
        print("Este animal salta")
    
    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un mamífero")
        else:
            print("No puedes comerte este animal")    


class Animal_de_granja(Mamifero):
    def __init__(self, comestible):
        super().__init__(comestible)  # Llamamos al constructor de la clase padre
        self.en_choza = False  # Agregamos el atributo adicional

    def guardar_en_choza(self):
        self.en_choza = True

    def sacar_de_choza(self):
        self.en_choza = False

    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un animal de granja")
        else:
            print("No puedes comerte este animal")


class Animal_domestico(Animal_de_granja):
    def __init__(self, nombre):
        super().__init__(False)  # Llamamos al constructor de la clase padre
        self.nombre = nombre
        self.en_casa = False
        self.patas = 3

    def guardar_en_casa(self):
        self.en_casa = True

    def sacar_de_casa(self):
        self.en_casa = False

    def me_lo_como(self):
        print(f"No te puedes comer a {self.nombre}")
        raise NotImplementedError("Este método no está disponible en la subclase")


# Los objetos son instancias de su clase y de las clases de las que hereda su clase
isinstance(perro, Animal_domestico)
isinstance(perro, Animal_de_granja)
isinstance(perro, Mamifero)

isinstance(cerdo, Animal_domestico)
isinstance(cerdo, Animal_de_granja)
isinstance(cerdo, Mamifero)

isinstance(ciervo, Animal_domestico)
isinstance(ciervo, Animal_de_granja)
isinstance(ciervo, Mamifero)

issubclass(Animal_domestico, Animal_de_granja)
issubclass(Animal_de_granja, Mamifero)
issubclass(Animal_domestico, Mamifero)

#############
# Ejercicio #
#___________#
# Si transferimos a nuestra aplicacion de personal, puedo crear la clase empleado
# y a partir de ella crear clases herederas según cargo.


# Las clases "hijo" serán Directivo, Oficinista, Peon

# El directivo, tiene coche de empresa, y métodos asociados a él.
# El oficinista tiene bonuses
# El peón tiene guardias... etc
from POO.personal import Empleado
from POO.activos import Coche
class Directivo(Empleado):
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
        self.coche_empresa = Coche("Renault", "Megane", 3.5, 3000)
   

def asignar_coche(self):
    print(f"{self.nombre} tiene {self.coche_empresa}.")

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
# Asignar guardias al peon si ficha mas tarde de las 21:00

    def asignar_guardias(self, cantidad):
        import datetime
        hora_actual = datetime.datetime.now()
        if hora_actual.hour >= 21:
            print(f"{self.nombre} ha fichado tarde. Asignando {cantidad} guardias.")    
        self.guardias += cantidad
        print(f"{self.nombre} ha recibido {cantidad} guardias. Total guardias: {self.guardias}")
        # Con cada guardia el peón cobra 10 euros
        print(f"{self.nombre} ha cobrado {cantidad * 10} euros por {cantidad} guardias. Total guardias: {self.guardias}")   

personal(empleado_directivo("Juan"))
personal(empleado_oficinista("Ana"))
personal(empleado_peon("Luis"))
# Creando instancias de las clases heredadas
juan_directivo = Directivo("Juan")
ana_oficinista = Oficinista("Ana")
luis_peon = Peon("Luis")
juan_directivo.asignar_coche()
ana_oficinista.asignar_bonus(500)
# peon.ficha()  # No existe el método ficha en la clase Peon, así que esta línea se comenta o elimina
luis_peon.asignar_guardias()

# Verificando las instancias
print(isinstance(juan_directivo, Directivo))  # True
print(isinstance(ana_oficinista, Oficinista))  # True
print(isinstance(luis_peon, Peon))  # True


# Codigo Aitor 
director = Directivo('Juan', 'Pérez', 'López')

secretario = Oficinista('Juanito', 'Pérez', 'García')

# El directivo, tiene coche de empresa, y métodos asociados a él.
director.coche_empresa = Coche("Mercedes", "Maybach", 4.5,100000)
director.asigna_gasolina(300)

director.ficha()
director.ficha()
director.calcula_trabajo()
director.calcula_sueldo()
director.coche_empresa.marca
director.coche_empresa.presentarse()

# El oficinista tiene bonuses
secretario = Oficinista('Juanito', 'Pérez', 'García')
secretario.ficha()
secretario.ficha()
secretario.calcula_trabajo()
secretario.asigna_bonus(100)
secretario.calcula_sueldo()


# El peón tiene guardias... etc
peon = Peon('Pepe', 'Pérez', 'García')


peon.ficha()
peon.guardias
peon.ficha()
peon.guardias