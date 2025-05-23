# Ejercicio 1: Saludo Personalizado
"""
1. Pide al usuario que ingrese su nombre.
2. Pide al usuario que ingrese su fecha de nacimiento. (día/mes/año)
3. Convierte el dato aportado por el usuario en un objeto datetime (consulta la documentación)
4. Calcula la edad del usuario.
5. Muestra un mensaje de bienvenida formateado que incluya su nombre, edad y año de nacimiento.
    - Ejemplo: "¡Hola, [Nombre]! Tienes [Edad] años y naciste en [AñoNacimiento]."
"""
import datetime

datetime.datetime.now()

hoy = datetime.date.today()

nacimiento = datetime.date(2000, 5, 25)

# nacimiento.year = 2025

cumpleannos = datetime.date(hoy.year, nacimiento.month, nacimiento.day)

(hoy - cumpleannos).days

def calcular_edad(nacimiento: datetime.date) -> int:
    """
    Calcula la edad de una persona a partir de su fecha de nacimiento.
    :param nacimiento: Fecha de nacimiento en formato datetime.date.
    :return: Edad de la persona.
    """
    hoy = datetime.date.today()
    
    # Calcula la fecha del cumpleaños en el año actual
    cumpleannos = datetime.date(hoy.year, nacimiento.month, nacimiento.day)
    
    # Calcula la edad por diferencia de año de nacimiento
    edad = hoy.year - nacimiento.year
    
    # Si el cumpleaños no ha llegado aún este año, restar un año a la edad
    dias_desde_cumple = (hoy - cumpleannos).days
    edad -= 1 if dias_desde_cumple < 0 else 0
    
    # Si hoy es el cumpleaños, felicitar
    if dias_desde_cumple==0:
        print("¡Feliz cumpleaños!")
    return edad


def saludo_personalizado():
    print("Hola, bienvenido al programa de saludo personalizado.")
    nombre = input("Por favor, ingresa tu nombre: ")
    nacimiento_str = input("Ingresa tu fecha de nacimiento (día/mes/año): ")
    nacimiento_fecha = datetime.datetime.strptime(nacimiento_str, "%d/%m/%Y")
    edad = calcular_edad(nacimiento_fecha)
    print(f"¡Hola, {nombre}! Tienes {edad} años pero aparentas mucho menos y naciste en {nacimiento_fecha.year}.")

(4,30) < (5,1)

saludo_personalizado()
22

#Ejercicio 2: Operaciones con Cadenas#
"""
1. Pide al usuario que ingrese una frase.
2. Muestra:
    - La longitud de la frase.
    - La frase en mayúsculas.
    - La frase en minúsculas.
    - Las tres primeras letras de la frase.
    - Las tres últimas letras de la frase.
    - La frase con todas las 'a' reemplazadas por una 'e'.
"""
import re
def pide_frase():
    frase = input("Ingresa una frase: ")
    print(f"La longitud de la frase es: {len(frase)}")
    print(f"La frase en mayúsculas es: {frase.upper()}")
    print(f"La frase en minúsculas es: {frase.lower()}")
    print(f"Las tres primeras letras de la frase son: {frase[:3]}")
    print(f"Las tres últimas letras de la frase son: {frase[-3:]}")
    print(f"La frase con todas las 'a' reemplazadas por una 'e' es: {frase.replace('a', 'e')}")
    print(f"La frase con todas las 'a' reemplazadas por una 'e' son regex es: {re.sub('[aá]', 'e', frase)}")
    return frase

pide_frase()

#Ejercicio 3: Información de Contacto (Diccionario)#
"""
1. Crea un diccionario llamado `contacto` que almacene:
    - `nombre`: (pide al usuario que lo ingrese)
    - `telefono`: (pide al usuario que lo ingrese)
    - `email`: (pide al usuario que lo ingrese)
2. Muestra la información del contacto de forma clara (ej: "Nombre: Juan, Teléfono: 123456789, Email: [juan@example.com](mailto:juan@example.com)").
3. Pregunta al usuario si quiere añadir una `ciudad` al contacto. Si es así, pídela y añádela al diccionario.
4. Muestra todas las claves (keys) del diccionario.
5. Muestra todos los valores (values) del diccionario.
"""

def verifica_telefono(telefono):
    while True:
        telefono_num = "".join(filter(str.isdigit, telefono))
        if len(telefono_num) == 9 and telefono_num[0] in "679":
            return telefono_num
        else:
            telefono = input("El teléfono no es correcto. Introduce un teléfono correcto: ")

verifica_telefono("1234sdfsgsd .56e789")

def contacto():
    # 1. Crear el diccionario contacto
    contacto = {
        'nombre': input("Ingrese el nombre: "),
        'telefono': verifica_telefono(input("Ingrese el teléfono: ")),
        'email': input("Ingrese el email: ")
    }

    # 2. Mostrar la información del contacto
    print(f"\nInformación del contacto:")
    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

    # 3. Preguntar por ciudad
    agregar_ciudad = input("\n¿Desea añadir una ciudad al contacto? (s/n): ").lower()
    if agregar_ciudad == 's':
        contacto['ciudad'] = input("Ingrese la ciudad: ")
        print("¡Ciudad añadida correctamente!")

    # 4. Mostrar todas las claves
    print("\nClaves del diccionario:", list(contacto.keys()))  # Convertimos a lista para mejor visualización

    # 5. Mostrar todos los valores
    print("\nValores del diccionario:", list(contacto.values()))

    return contacto

contacto_resultante = contacto()
print("Diccionario final completo:", contacto_resultante)