#1. Definir la Clase Abstracta MaterialBiblioteca :
#Atributos comunes: titulo , autor , codigo_inventario .
#Métodos comunes: mostrar_info (método abstracto).
from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, codigo_inventario, ubicacion):
        self.titulo = titulo
        self.__ubicacion = ubicacion
        self.codigo_inventario = codigo_inventario
        self.disponible = True

    @property
    def ubicacion(self):
        print(f"Tienes permiso para ver la ubicacion del item '{self.titulo}'.")
        return self.__ubicacion
    
    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        print(f"Compruebo que la ubicación está disponible para el item '{self.titulo}'.")
        self.__ubicacion = nueva_ubicacion

    def trasladar(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"El item '{self.titulo}' ha sido trasladado a '{nueva_ubicacion}'.")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El item '{self.titulo}' ha sido prestado.")
        else:
            print(f"El item '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El item '{self.titulo}' ha sido devuelto.")
    
    @abstractmethod
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Código de inventario: {self.codigo_inventario}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo_inventario, autor, isbn, numero_paginas):
        super().__init__(titulo, codigo_inventario, ubicacion=None)
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.isbn = isbn
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Número de páginas: {self.numero_paginas}")


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo_inventario, fecha_publicacion, numero_edicion):
        super().__init__(titulo, codigo_inventario, ubicacion=None)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número: {self.numero_edicion}")
        print(f"Fecha de publicación: {self.fecha_publicacion}")

class DVD(MaterialBiblioteca):
    def __init__(self, titulo, codigo_inventario, duracion, director):
        super().__init__(titulo, codigo_inventario, ubicacion=None)
        self.duracion = duracion
        self.director = director
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Duración: {self.duracion} minutos")
        print(f"Director: {self.director}")

import pickle
class GestorBiblioteca:
    def __init__(self):
        self.materiales = self.cargar_materiales()
    
    def almacenar_materiales(self):
        pickle.dump(self.materiales, open("materiales_biblioteca.pkl", "wb"))
        for material in self.materiales:
            print(f"Material '{material.titulo}' almacenado en el archivo.")

    def cargar_materiales(self):
            try:
                materiales = pickle.load(open("materiales_biblioteca.pkl", "rb"))
                print("Materiales cargados desde el archivo.")
                return materiales
            except FileNotFoundError:
                print("No se encontró el archivo de materiales.")
                return []
    
        
    def borrar_materiales(self,codigo_inventario=None):
        if codigo_inventario:

            self.materiales = []
            print("Todos los materiales han sido borrados.")
            self.almacenar_materiales()
