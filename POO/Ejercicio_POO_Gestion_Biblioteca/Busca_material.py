# Busca_material.py
'''from Ejercicio_POO_Gestion_Biblioteca.MaterialBiblioteca import Libro, Revista, DVD

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
'''
from MaterialBiblioteca import GestorBiblioteca, Libro, Revista, DVD, Usuario

import uuid

app = GestorBiblioteca()
while True:
    print("1. Agregar material")
    print("2. Listar materiales")
    print("3. Buscar material")
    print("4. Borrar material")
    print("5. Agregar_usuario")
    print("6. Listar usuarios")
    print("7. Agregar préstamo")
    print("8. Listar préstamos")
    print("q. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        tipo = input("Ingrese el tipo de material (libro, revista, DVD): ").lower()
        titulo = input("Ingrese el título: ")
        codigo_inventario = uuid.uuid4().hex[:6].upper()  # Genera un código único
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
        app.agregar_material(material)
        print(f"Material '{material.titulo}' agregado a la biblioteca.")
    elif opcion == '2':
        app.mostrar_materiales()
    elif opcion == '3':
        codigo_inventario = input("Ingrese el codigo_inventario del material: ")
        app.buscar_material(codigo_inventario)
    elif opcion == '4':
        codigo_inventario = input("Ingrese el codigo_inventario del material a borrar: ")
        app.borrar_material(codigo_inventario)
    elif opcion == '5':
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        usuario = Usuario(nombre, apellido)
        app.agregar_usuario(usuario)
        print(f"Usuario '{usuario.nombre}' agregado a la biblioteca.")
    elif opcion == '6':
        app.mostrar_usuarios()
    elif opcion == '7':
        id_usuario = input("Ingrese id_usuario del usuario: ")
        id_material = input("Ingrese id_material del material: ")
        app.prestar_material(id_usuario, id_material)
    elif opcion == '8':
        app.mostrar_prestamos()
    elif opcion == 'q':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

