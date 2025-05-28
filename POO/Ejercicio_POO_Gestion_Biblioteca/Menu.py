from MaterialBiblioteca  import MaterialBiblioteca
from MaterialBiblioteca import Libro,Revista,DVD



from datetime import date


class BuscaMaterial:
    def __init__(self):
        self.materiales = []
        # Materiales de ejemplo
        libro1 = Libro("El Quijote", "Miguel de Cervantes", "12345", "978-3-16-148410-0", 500)
        revista1 = Revista("National Geographic", "67890", date(2010, 7, 16), 125)
        dvd1 = DVD("Inception", "11223", 148, "Christopher Nolan")
        self.materiales.extend([libro1, revista1, dvd1])

    def menu(self):
        print("Bienvenido a la Biblioteca")
        print("1. Agregar Material")
        print("2. Listar Materiales")
        print("3. Buscar Material por Título")
        print("4. Mostrar Información de un Material")
        print("5. Salir")
        
        while True:
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.agregar_material()
                print("Agregando material...")
                agregar_material = MaterialBiblioteca.MaterialBiblioteca()
                agregar_material.agregar_material()
                print("Material agregado exitosamente.")
            elif opcion == '2':
                self.listar_materiales()
                listar_materiales = MaterialBiblioteca.MaterialBiblioteca()
                listar_materiales.listar_materiales()
            elif opcion == '3':
                self.buscar_material()
            elif opcion == '4':
                self.mostrar_informacion_material()
            elif opcion == '5':
                print("Gracias por usar la Biblioteca. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")  

    # Métodos para agregar, listar, buscar y mostrar información de materiales
    def agregar_material(self):
        input("Introduce el tipo de material ")
        print("Agregando material...")

    def listar_material_por_codigo(self, codigo_inventario):
        # Suponiendo que tienes una lista llamada self.materiales con todos los materiales agregados
        encontrados = [mat for mat in self.materiales if mat.get_codigo_inventario() == codigo_inventario]
        if encontrados:
            print(f"Material(es) con código {codigo_inventario}:")
            for mat in encontrados:
                mat.mostrar_info()
        else:
            print(f"No se encontró material con el código {codigo_inventario}.")
        codigo = input("Introduce el código de inventario a buscar: ")
        self.listar_material_por_codigo(codigo)

    def buscar_material(self):
        codigo = input("Introduce el código de inventario a buscar: ")
        self.listar_material_por_codigo(codigo)

    def mostrar_informacion_material(self):
        codigo = input("Introduce el código de inventario del material: ")
        encontrado = next((mat for mat in self.materiales if mat.get_codigo_inventario() == codigo), None)
        if encontrado:
            print("Información del Material:")
            print(encontrado.mostrar_info())
        else:
            print(f"No se encontró material con el código {codigo}.")

    def mostrar_tabla_materiales(self, materiales):
        if not materiales:
            print("No hay materiales para mostrar.")
            return
        print(f"{'Título':<30} {'Autor':<20} {'Código Inventario':<20}")
        print("-" * 70)
        for mat in materiales:
            print(f"{mat.get_titulo():<30} {mat.get_autor():<20} {mat.get_codigo_inventario():<20}")

    # Ejemplo de uso dentro de tu clase:
    def listar_materiales(self):
        # Suponiendo que tienes una lista self.materiales
        self.mostrar_tabla_materiales(self.materiales)