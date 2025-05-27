#1. Definir la Clase Abstracta MaterialBiblioteca :
#Atributos comunes: titulo , autor , codigo_inventario .
#Métodos comunes: mostrar_info (método abstracto).
class MaterialBiblioteca:
    def comun__init__(self, titulo, autor, codigo_inventario):
        self.titulo = titulo
        self.autor = autor
        self.codigo_inventario = codigo_inventario

    def adicional_info_libro(self, numero_paginas):
        self.numero_paginas = numero_paginas
        if not isinstance(numero_paginas, int) or numero_paginas <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo.")   
        return f"Este libro tiene {numero_paginas} páginas."
    def adicional_info_revista(self, numero_edicion, fecha_publicacion):
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion
        if not isinstance(numero_edicion, int) or numero_edicion <= 0:
            raise ValueError("El número de edición debe ser un entero positivo.")
        return f"Esta revista es la edición {numero_edicion} publicada en {fecha_publicacion}."
    def adicional_info_dvd(self, duracion, formato):
        self.duracion = duracion
        self.formato = formato
        return f"Este DVD tiene una duración de {duracion} minutos y un formato de {formato}."
    

    def __str__(self):
        return f"{self.titulo} por {self.autor}, codigo de inventario: {self.codigo_inventario},"
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    def get_numero_paginas(self):
        return self.numero_paginas
    
    def get_codigo_inventario(self):
        return self.codigo_inventario  

    def get_numero_edicion(self):
        return self.numero_edicion  
    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    def get_duracion(self):
        return self.duracion
    def get_formato(self):
        return self.formato
from abc import ABC, abstractmethod
class MaterialBiblioteca(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass 

    def libro(self):
        return f"Libro: {self.titulo} por {self.autor}, codigo de inventario: {self.codigo_inventario},tiene {self.numero_paginas}, " 

    def revista(self):
        return f"Revista: {self.titulo}, edicion {self.numero_edicion}, codigo de inventario: {self.codigo_inventario}, "
    def dvd(self):
        return f"DVD: {self.titulo}, duracion {self.duracion} minutos, formato {self.formato}, codigo de inventario: {self.codigo_inventario}, "   
    #Proteger los atributos con __ (doble guion bajo) y proporcionar métodos getters y setters .
      # Getters y setters protegidos
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_codigo_inventario(self):
        return self.__codigo_inventario

    def set_codigo_inventario(self, codigo):
        self.__codigo_inventario = codigo