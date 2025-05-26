'''
Ejercicio 1: Saludo Personalizado
1. Pide al usuario que ingrese su nombre.
2. Pide al usuario que ingrese su fecha de nacimiento. (día/mes/año)
3. Convierte el dato aportado por el usuario en un objeto datetime (consulta la documentación)
4. Calcula la edad del usuario.
5. Muestra un mensaje de bienvenida formateado que incluya su nombre, edad y año de
nacimiento.
Ejemplo: "¡Hola, [Nombre]! Tienes [Edad] años y naciste en [AñoNacimiento]."

'''
def saludo_personalizado():
    from datetime import datetime
    # Pedir el nombre y la fecha de nacimiento al usuario
    nombre = input("Ingresa tu nombre: ")
    fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (día/mes/año): ")

    # Convertir la cadena a un objeto datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    
    # Calcular la edad
    edad = (datetime.now() - fecha_nacimiento).days // 365
    
    # Mostrar el mensaje formateado
    print(f"¡Hola, {nombre}! Tienes {edad} años y naciste en {fecha_nacimiento.year}.")
# Llamar a la función
# para ejecutar el saludo personalizado
    if __name__ == "__main__":
        saludo_personalizado()
    


'''
Ejercicio 2: Operaciones con Cadenas
1. Pide al usuario que ingrese una frase.
2. Muestra:
La longitud de la frase.
La frase en mayúsculas.
La frase en minúsculas.
Las tres primeras letras de la frase.
Las tres últimas letras de la frase.
La frase con todas las 'a' reemplazadas por una 'e'.
'''

def operaciones_con_cadenas():
    frase = input("Ingrese una frase: ")
    print(f"La longitud de la frase es: {len(frase)}")
    print(f"La frase en mayúsculas es: {frase.upper()}")
    print(f"La frase en minúsculas es: {frase.lower()}")
    print(f"Las tres primeras letras de la frase son: {frase[:3]}")
    print(f"Las tres últimas letras de la frase son: {frase[-3:]}")
    print(f"La frase con todas las 'a' reemplazadas por una 'e': {frase.replace('a', 'e')}")

operaciones_con_cadenas()


'''
Ejercicio 3: Información de Contacto (Diccionario)
1. Crea un diccionario llamado contacto que almacene:
nombre : (pide al usuario que lo ingrese)
telefono : (pide al usuario que lo ingrese)
email : (pide al usuario que lo ingrese)

2. Muestra la información del contacto de forma clara (ej: "Nombre: Juan, Teléfono: 123456789,
Email: juan@example.com").
3. Pregunta al usuario si quiere añadir una ciudad al contacto. Si es así, pídela y añádela al
diccionario.
4. Muestra todas las claves (keys) del diccionario.
5. Muestra todos los valores (values) del diccionario. formateo de string
'''
def informacion_contacto():
    contacto = {}
    contacto["nombre"] = input("Ingrese el nombre: ")
    contacto["telefono"] = input("Ingrese el telefono: ")
    contacto["email"] = input("Ingrese el email: ")
    return contacto

def agregar_ciudad(contacto):
    respuesta = input("¿Desea añadir una ciudad al contacto? (si/no): ")
    if respuesta.lower() == "si":
        contacto["ciudad"] = input("Ingrese la ciudad: ")
        print(f"Ciudad añadida: {contacto['ciudad']}")

def mostrar_claves(contacto):
    print("Claves del diccionario:")
    print(", ".join(contacto.keys()))

def mostrar_valores(contacto):
    print("Valores del diccionario:")
    print(", ".join(str(valor) for valor in contacto.values()))

# Ejecución ordenada
if __name__ == "__main__":
    contacto = informacion_contacto()
    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    agregar_ciudad(contacto)
    mostrar_claves(contacto)
    mostrar_valores(contacto)


'''
Ejercicio 4: Elementos Únicos (Sets)
1. Crea una lista con elementos duplicados, por ejemplo: numeros = [1, 2, 2, 3, 4, 4, 4, 5] .
2. Convierte esta lista a un set para eliminar los duplicados.
3. Muestra el set resultante.
4. Crea otro set con algunos números, por ejemplo: otros_numeros = {4, 5, 6, 7} .
5. Muestra la unión de ambos sets.
6. Muestra la intersección de ambos sets.

'''

lista_random = [1, 2, 2, 3, 4, 4, 4, 5]
set_random = set(lista_random)
print(f"Lista original: {lista_random}")
lista_random2 = [ 1,1,2,3,4,4,5,6,7,8,9]
set_random2 = set(lista_random2)
print(f"Lista sin duplicados: {set_random}")
print(f"Union: {set_random | set_random2}")
print(f"Interseccion: {set_random & set_random2}")


'''
Ejercicio 5: Menú de Opciones (con match )
1. Muestra un menú de opciones al usuario:
1. Escribir texto en un archivo
2. Mostrar el texto escrito un archivo
3. Mostrar fecha actual
4. Salir del programa
2. Pide al usuario que elija una opción (1, 2 o 3).
3. Usa una estructura match-case para ejecutar la acción correspondiente a la opción elegida.
4. Si la opción no es válida, muestra un mensaje de error.
'''

def escribir_archivo():
    texto = input("Introduce el texto que deseas guardar en el archivo: ")
    with open("archivo_texto.txt", "w", encoding="utf-8") as f:
        f.write(texto)
    print("Texto guardado correctamente en archivo_texto.txt.")

def mostrar_archivo():
    try:
        with open("archivo_texto.txt", "r", encoding="utf-8") as f:
            contenido = f.read()
        print("Contenido del archivo:")
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe. Escribe primero algún texto.")

def mostrar_fecha_actual():
    from datetime import datetime
    print("Fecha y hora actual:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def menu_opciones():
    while True:
        print("Menú de opciones:")
        print("1. Escribir texto en un archivo")
        print("2. Mostrar el texto escrito en un archivo")
        print("3. Mostrar fecha actual")
        print("4. Salir del programa")

        opcion = input("Elige una opción (1-4): ")

        match opcion:
            case "1":
                escribir_archivo()
            case "2":
                mostrar_archivo()
            case "3":
                mostrar_fecha_actual()
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
# Llamar a la función para ejecutar el menú
if __name__ == "__main__":
    menu_opciones()


'''
Ejercicio 6: Lista de la Compra
1. Crea una lista vacía llamada lista_compra .
2. Pide al usuario que ingrese 5 productos para añadir a la lista.
3. Muestra la lista completa.
4. Pregunta al usuario si quiere eliminar algún producto. Si dice que sí, pregúntale cuál y elimínalo.
5. Muestra la lista final.
6. Indica cuántos productos quedan en la lista.
7. Mantén sincronizada la lista con un archivo tareas.txt
8. Utiliza el bloque with open(...) para asegurar que los archivos se cierren correctamente.
9. Utiliza try-except para manejar posibles FileNotFoundError si el archivo no existe al intentar leerlo por
primera vez (en ese caso, simplemente informa que no hay tareas).

'''
def lista_compra():
    lista_compra = []
    for i in range(5):
        producto = input(f"Ingrese el producto {i + 1}: ")
        lista_compra.append(producto)
    
    print("Lista de la compra:", lista_compra)
    
    eliminar = input("¿Desea eliminar algún producto? (si/no): ")
    if eliminar.lower() == "si":
        producto_eliminar = input("¿Cuál producto desea eliminar?: ")
        if producto_eliminar in lista_compra:
            lista_compra.remove(producto_eliminar)
            print(f"Producto '{producto_eliminar}' eliminado.")
        else:
            print(f"El producto '{producto_eliminar}' no está en la lista.")
    
    print("Lista final:", lista_compra)
    print(f"Quedan {len(lista_compra)} productos en la lista.")
    
    # Guardar la lista en un archivo
    with open("tareas.txt", "w", encoding="utf-8") as f:
        for item in lista_compra:
            f.write(item + "\n")
    
    # Leer el archivo y mostrar su contenido
    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            contenido = f.read()
        print("Contenido del archivo tareas.txt:")
        print(contenido)
    except FileNotFoundError:
        print("El archivo tareas.txt no existe. No hay tareas guardadas.")

if __name__ == "__main__":
    lista_compra()

'''
Ejercicio 7:
Desafío: Contador de Palabras en un Archivo



1. Pide al usuario el nombre de un archivo de texto.
2. Lee el contenido del archivo.
3. Limpia el texto: conviértelo a minúsculas y elimina signos de puntuación básicos (puedes usar
replace() para comas, puntos, etc.).
4. Divide el texto en palabras.
5. Usa un diccionario para contar la frecuencia de cada palabra.
6. Muestra las 10 palabras más frecuentes y su conteo.
7. Maneja la excepción FileNotFoundError .

'''
def contador_palabras():
    from collections import Counter
    import string

    # Pide al usuario el nombre del archivo
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

    try:
        # Lee el contenido del archivo
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()

        # Limpia el texto: convierte a minúsculas y elimina signos de puntuación
        contenido = contenido.lower()
        contenido = contenido.translate(str.maketrans("", "", string.punctuation))

        # Divide el texto en palabras
        palabras = contenido.split()

        # Usa un diccionario para contar la frecuencia de cada palabra
        contador = Counter(palabras)

        # Muestra las 10 palabras más frecuentes y su conteo
        print("Las 10 palabras más frecuentes son:")
        for palabra, conteo in contador.most_common(10):
            print(f"{palabra}: {conteo}")

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

    contador_palabras()
    
    