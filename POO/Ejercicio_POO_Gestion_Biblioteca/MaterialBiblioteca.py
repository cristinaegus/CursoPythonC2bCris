#1. Definir la Clase Abstracta MaterialBiblioteca :
#Atributos comunes: titulo , autor , codigo_inventario .
#Métodos comunes: mostrar_info (método abstracto).
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

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

import uuid
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = uuid.uuid4().hex[:6].upper()  # Genera un ID único
    
    def mostrar_info(self):
        print(f"{self.nombre} {self.apellido} ID Usuario: {self.id_usuario}")
class Prestamo:
    def __init__(self,id_prestamo, usuario, material):
    
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = datetime.now() + timedelta(days=14)  # 2 semanas de préstamo   

def mostrar_info(self):
    print(f"ID de préstamo: {self.id_prestamo}")
    print(f"Usuario: {self.usuario.nombre} {self.usuario.apellido}")
    print(f"Material: {self.material.titulo}")
    print(f"Fecha de préstamo: {self.fecha_prestamo}")
    print(f"Fecha de devolución: {self.fecha_devolucion}")
import pickle
class GestorBiblioteca:
    def __init__(self):
        self.materiales = self.cargar_materiales()
        self.usuarios = self.cargar_usuarios()
        self.prestamos = self.cargar_prestamos()
    
    def almacenar_materiales(self):
        pickle.dump(self.materiales, open("materiales_biblioteca.pkl", "wb"))
        for material in self.materiales:
            print(f"Material '{material.titulo}' almacenado en el archivo.")

    def almacenar_usuarios(self, usuarios):
        with open("usuarios_biblioteca.pkl", "wb") as file:
            pickle.dump(usuarios, file)
        print("Usuarios almacenados en el archivo.")

    def almacenar_prestamos(self):
        with open("prestamos_biblioteca.pkl", "wb") as archivo:
            pickle.dump(self.prestamos, archivo)

    def cargar_materiales(self):
        try:
            materiales = pickle.load(open("materiales_biblioteca.pkl", "rb"))
            print("Materiales cargados desde el archivo.")
            return materiales
        except FileNotFoundError:
            print("No se encontró el archivo de materiales.")
            return []
    
    def cargar_usuarios(self):
        try:
            usuarios = pickle.load(open("usuarios_biblioteca.pkl", "rb"))
            print("Usuarios cargados desde el archivo.")
            return usuarios
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios.")
            return []
    def cargar_prestamos(self):
        try:
            prestamos = pickle.load(open("prestamos_biblioteca.pkl", "rb"))
            print("Prestamos cargados desde el archivo.")
            return prestamos
        except FileNotFoundError:
            print("No se encontró el archivo de prestamos.")
            return []
    def agregar_material(self, material):
        self.materiales.append(material)
        self.almacenar_materiales()

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.almacenar_usuarios()
    
    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
        self.almacenar_prestamos()

    def borrar_material(self, codigo_inventario):
        borrables = [material for material in self.materiales if material.codigo_inventario == codigo_inventario]
        print("¿Está seguro de querer borrar estos materiales?")
        for material in borrables:
            material.mostrar_info()
        confirmacion = input("Ingrese 'si' para confirmar: ")
        if confirmacion.lower() == 'si':
            for material in borrables:
                self.materiales.remove(material)
            print("Materiales borrados.")
        self.almacenar_materiales()

    def mostrar_materiales(self):
        for material in self.materiales:
            material.mostrar_info()

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            usuario.mostrar_info()
    
    def buscar_material(self, codigo_inventario):
        for material in self.materiales:
            if material.codigo_inventario == codigo_inventario:
                material.mostrar_info()
                return
        print("Material no encontrado.") 

    def prestar_material(self, id_usuario, id_material):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        material = next((m for m in self.materiales if m.codigo_inventario == id_material), None)
        if usuario and material:
            prestamo = Prestamo(usuario, material)
            self.agregar_prestamo(prestamo)
        else:
            print("Usuario o material no encontrado.")

    def mostrar_prestamos(self):
        for prestamo in self.prestamos:
            prestamo.mostrar_info()
    # Clase Prestamo agregada para evitar el error de definición
    class Prestamo:
        def __init__(self, usuario, material):
            self.usuario = usuario
            self.material = material
            self.fecha_prestamo = datetime.now()
            self.devuelto = False
    
        def mostrar_info(self):
            print(f"Usuario: {getattr(self.usuario, 'nombre', str(self.usuario))}")
            print(f"Material: {self.material.titulo}")
            print(f"Fecha de préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Devuelto: {'Sí' if self.devuelto else 'No'}")

    def mostrar_prestamos(self):
        for prestamo in self.prestamos:
            prestamo.mostrar_info()     