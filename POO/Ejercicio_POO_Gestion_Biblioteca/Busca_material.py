# Busca_material.py
from Ejercicio_POO_Gestion_Biblioteca.MaterialBiblioteca import Libro, Revista, DVD

from MaterialBiblioteca import Libro, Revista, DVD

from datetime import date

libro1 = Libro("El Quijote", "12345", "Miguel de Cervantes", "978-3-16-148410-0", 500)
revista1 = Revista("National Geographic", "67890", date(2010, 7, 16), 125)
dvd1 = DVD("Inception", "11223", 148, "Christopher Nolan")

libro1.mostrar_info()
revista1.mostrar_info()
dvd1.mostrar_info()
libro1.prestar()
libro1.mostrar_info()
libro1.devolver()
libro1.mostrar_info()   

libro1.trasladar("Sala de Lectura")
libro1.mostrar_info()


lista_materiales = [libro1, revista1, dvd1]
for elemento in lista_materiales:
    elemento.mostrar_info()


libro1.trasladar("Sala de Lectura")
libro1.mostrar_info()

# guardar los materiales en un archivo usando pickle
import pickle

def almacenar_materiales(materiales):
    pickle.dump(materiales, open("materiales_biblioteca.pkl", "wb"))
    for material in materiales:
        print(f"Material '{material.titulo}' almacenado en el archivo.")

def cargar_materiales():
    try:
        materiales = pickle.load(open("materiales_biblioteca.pkl", "rb"))
        print("Materiales cargados desde el archivo.")
        return materiales
    except FileNotFoundError:
        print("No se encontró el archivo de materiales.")
        return []

materiales_cargados_del_archivo = cargar_materiales()
for material in materiales_cargados_del_archivo:
    material.mostrar_info()

lista_materiales =  cargar_materiales()

from MaterialBiblioteca import GestorBiblioteca

app = GestorBiblioteca()
while True:
    print("1. Agregar material")
    print("2. Listar materiales")
    print("3. Buscar material")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        tipo = input("Ingrese el tipo de material (libro, revista, DVD): ").lower()
        titulo = input("Ingrese el título: ")
        codigo_inventario = input("Ingrese el codigo_inventario: ")
        if tipo == 'libro':
            autor = input("Ingrese el autor: ")
            num_paginas = int(input("Ingrese el número de páginas: "))
            isbn = input("Ingrese el ISBN: ")
            material = Libro(titulo, codigo_inventario, autor, isbn, num_paginas)
        elif tipo == 'revista':
            fecha_publicacion = input("Ingrese la fecha de publicación: ")
            numero_edicion = input("Ingrese el número de edición: ")
            material = Revista(titulo, codigo_inventario, fecha_publicacion, numero_edicion)
        elif tipo == 'dvd':
            duracion = int(input("Ingrese la duración en minutos: "))
            director = input("Ingrese el director: ")
            material = DVD(titulo, codigo_inventario, duracion, director)
        else:
            print("Tipo de material no válido.")
            continue
        app.materiales.append(material)
        app.almacenar_materiales()
        print(f"Material '{material.titulo}' agregado a la biblioteca.")
    elif opcion == '2':
        for elemento in app.materiales:
            elemento.mostrar_info()
    elif opcion == '3':
        codigo_inventario = input("Ingrese el codigo_inventario del material: ")
        for material in app.materiales:
            if material.codigo_inventario == codigo_inventario:
                material.mostrar_info()
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
import uuid
#crea un ID único para el usuario
def crearId_usuario():
    return str(uuid.uuid4())[:8]  # Genera un ID único de 8 caracteres
# Función para registrar un usuario en la biblioteca incluido su ID


def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if not nombre_usuario:
        print("El nombre de usuario no puede estar vacío.")
        return None
    apellido_usuario = input("Ingrese su apellido: ")
    if not apellido_usuario:
        print("El apellido no puede estar vacío.")
        return None
    email_usuario = input("Ingrese su correo electrónico: ")
    if not email_usuario or '@' not in email_usuario:
        print("El correo electrónico no es válido.")
        return None
    id_usuario = crearId_usuario()
    print(f"ID de usuario generado: {id_usuario}")  
    print(f"Bienvenido {nombre_usuario} a la biblioteca.")
    return nombre_usuario
if __name__ == "__main__":
    id_usuario, nombre_usuario = registrar_usuario()
    if id_usuario and nombre_usuario:
        print(f"Usuario registrado con ID: {id_usuario} y nombre: {nombre_usuario}")
    else:
        print("Registro de usuario fallido.")
# Ejercicio POO: Gestión de Préstamos de Materiales en una Biblioteca
# Función para gestionar préstamos de materiales en la biblioteca
#Guardar los usuarios registrados en un archivo usando pickle
import pickle
def almacenar_usuarios(usuarios):
    with open("usuarios_biblioteca.pkl", "wb") as file:
        pickle.dump(usuarios, file)
    print("Usuarios almacenados en el archivo.")
def cargar_usuarios():
    try:
        with open("usuarios_biblioteca.pkl", "rb") as file:
            usuarios = pickle.load(file)
        print("Usuarios cargados desde el archivo.")
        return usuarios
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return []
def gestionar_prestamos(id_usuario, nombre_usuario,codigo_inventario):
 
 while True:
    usuarios = cargar_usuarios()
    if not id_usuario or not nombre_usuario:
        print("Debe registrarse primero para gestionar préstamos.")
        return
    print(f"Bienvenido {id_usuario, nombre_usuario} a la gestión de préstamos de materiales.")
    codigo_inventario = input("Ingrese el codigo_inventario del material a prestar: ")
    for material in app.materiales:
        if material.codigo_inventario == codigo_inventario:
            material.prestar()
            print(f"Material '{material.titulo}' prestado.")
            return
    print("Material no encontrado.")