from Biblioteca import GestorBiblioteca, Libro, Revista, DVD, Usuario
from Biblioteca import Prestamo
import uuid



app = GestorBiblioteca()
while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar Usuario")
        print("2. Listar Usuarios")
        print("3. Agregar Material")
        print("4. Listar Materiales")
        print("5. Buscar Material por Código")
        print("6. Borrar Material")
        print("7. Agregar Préstamo")
        print("8. Listar Préstamos")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del usuario: ")
            apellido = input("Apellido del usuario: ")
            usuario = Usuario(nombre, apellido)
            app.almacenar_usuarios([usuario])
        
            print("Usuario agregado correctamente.")
        elif opcion == '2':
            app.mostrar_usuarios()
        elif opcion == '3':
            tipo = input("Tipo de material (libro, revista, dvd): ").lower()
            titulo = input("Título: ")
            codigo_inventario = uuid.uuid4().hex[:8].upper()
            if tipo == 'libro':
                autor = input("Autor: ")
                isbn = input("ISBN: ")
                num_paginas = int(input("Número de páginas: "))
                material = Libro(titulo, codigo_inventario, autor, isbn, num_paginas)
            elif tipo == 'revista':
                fecha_publicacion = input("Fecha de publicación (YYYY-MM-DD): ")
                numero_edicion = int(input("Número de edición: "))
                material = Revista(titulo, codigo_inventario, fecha_publicacion, numero_edicion)
            elif tipo == 'dvd':
                duracion = int(input("Duración en minutos: "))
                director = input("Director: ")
                material = DVD(titulo, codigo_inventario, duracion, director)
            else:
                print("Tipo de material no válido.")
                continue
            app.agregar_material(material)
            print("Material agregado correctamente.")
        elif opcion == '4':
            app.mostrar_materiales()
        elif opcion == '5':
            codigo = input("Ingrese el código de inventario a buscar: ")
            app.buscar_material(codigo)
        elif opcion == '6':
            codigo = input("Ingrese el código de inventario del material a borrar: ")
            app.borrar_material(codigo)
        elif opcion == '7':
            id_usuario = input("ID del usuario: ")
            id_material = input("Código de inventario del material: ")
            app.prestar_material(id_usuario, id_material)
        elif opcion == '8':
            app.mostrar_prestamos()
        elif opcion == '9':
            print("Gracias por usar la Biblioteca. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    app = GestorBiblioteca()

