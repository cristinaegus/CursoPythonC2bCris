from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from Mysqlconnection import get_connection
from uuid import uuid4


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


from datetime import datetime, timedelta
import random
import uuid
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = random.randint(1, 1000)  # Genera un ID único
    
    def mostrar_info(self):
        print(f"{self.nombre} {self.apellido} ID Usuario: {self.id_usuario}")


class Prestamo:
    def __init__(self, id_prestamo, usuario, material):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = datetime.now() + timedelta(days=14)  # 2 semanas de préstamo   
        self.usuarios = []
        self.prestamos = []
    def mostrar_info(self):
        print(f"ID de préstamo: {self.id_prestamo}")
        print(f"Usuario: {self.usuario.nombre} {self.usuario.apellido}")
        print(f"Material: {self.material.titulo}")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion}")
    

class GestorBiblioteca:
    def __init__(self):
        self.materiales = self.cargar_materiales()

    def almacenar_usuarios(self,usuarios):
        conn = get_connection()
        cursor = conn.cursor()
        for usuario in usuarios:
            cursor.execute("""
                INSERT INTO usuarios (id_usuario, nombre, apellido)
                VALUES (%s, %s, %s)
                ON CONFLICT (id_usuario) DO UPDATE
                SET nombre=EXCLUDED.nombre, apellido=EXCLUDED.apellido;
            """, (usuario.id_usuario, usuario.nombre, usuario.apellido))
        conn.commit()
        cursor.close()
        conn.close()
        print("Usuarios almacenados en la base de datos.")
    def almacenar_prestamos(self):
        conn = get_connection()
        cursor = conn.cursor()
        for prestamo in self.prestamos:
            cursor.execute("""
                INSERT INTO prestamos (id_prestamo, id_usuario, codigo_inventario, fecha_prestamo, fecha_devolucion)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id_prestamo) DO UPDATE
                SET id_usuario=EXCLUDED.id_usuario, codigo_inventario=EXCLUDED.codigo_inventario,
                    fecha_prestamo=EXCLUDED.fecha_prestamo, fecha_devolucion=EXCLUDED.fecha_devolucion;
            """, (prestamo.id_prestamo, prestamo.usuario.id_usuario, prestamo.material.codigo_inventario, prestamo.fecha_prestamo, prestamo.fecha_devolucion))
        conn.commit()
        cursor.close()
        conn.close()
        print("Préstamos almacenados en la base de datos.")
 
    def almacenar_materiales(self):
        # Inserta todos los materiales en la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        for material in self.materiales:
            cursor.execute("""
                INSERT INTO materiales (codigo_inventario, titulo, tipo, ubicacion, disponible)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (codigo_inventario) DO UPDATE
                SET titulo=EXCLUDED.titulo, tipo=EXCLUDED.tipo, ubicacion=EXCLUDED.ubicacion, disponible=EXCLUDED.disponible;
            """, (material.codigo_inventario, material.titulo, material.__class__.__name__.lower(), material.ubicacion, material.disponible))
        conn.commit()
        cursor.close()
        conn.close()
        print("Materiales almacenados en la base de datos.")



    def cargar_materiales(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo_inventario, titulo, tipo, ubicacion, disponible FROM materiales;")
        rows = cursor.fetchall()
        materiales = []
        for row in rows:
            tipo = row[2]
            if tipo == "libro":
                # Aquí deberías hacer un JOIN para obtener los datos específicos de libro
                materiales.append(Libro(row[1], row[0], "Autor", "ISBN", 0))  # Completa según tu modelo real
            elif tipo == "revista":
                materiales.append(Revista(row[1], row[0], "Fecha", 0))
            elif tipo == "dvd":
                materiales.append(DVD(row[1], row[0], 0, "Director"))
        cursor.close()
        conn.close()
        print("Materiales cargados desde la base de datos.")
        return materiales
    
    
if __name__ == "__main__":
   
   ''' usuario1 = Usuario("Juan", "Pérez")
    biblioteca = GestorBiblioteca()
    biblioteca.usuarios.append(usuario1)
    '''
   

