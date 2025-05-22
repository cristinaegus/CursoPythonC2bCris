# Ejercicio 1
"""
Crea una lista llamada 'dias' con los días de la semana.
Luego imprime el primer y el último elemento de la lista.
"""

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Primer día:", dias[0])
print("Último día:", dias[-1])

# Ejercicio 2
"""
Modifica el segundo y el quinto elemento de la lista 'dias' para que estén en inglés.
Imprime la lista modificada.
"""

dias[1] = "Tuesday"
dias[4] = "Friday"
print(dias)

# Ejercicio 3
"""
Crea una lista vacía llamada 'numeros'.
Usa un bucle for para llenarla con los números del 1 al 5.
Luego imprime la lista.
"""

numeros = []
for i in range(1, 6):
    numeros.append(i)
print(numeros)

# Ejercicio 4
"""
Extrae los tres primeros elementos de la lista 'dias' y guárdalos en una nueva lista llamada 'inicio_semana'.
Imprime esa nueva lista.
"""

inicio_semana = dias[:3]
print("Inicio de la semana:", inicio_semana)

# Ejercicio 5
"""
Verifica si "Domingo" está en la lista 'dias'.
Si está, imprime "¡Encontrado!".
Si no está, imprime "No está en la lista.".
"""

if "Domingo" in dias:
    print("¡Encontrado!")
else:
    print("No está en la lista.")

# Ejercicio 6
"""
Concatena la lista [8, 9, 10] a la lista 'numeros'.
Imprime la nueva lista.
"""

numeros = numeros + [8, 9, 10]
print("Lista extendida:", numeros)

# Ejercicio 7
"""
Cuenta cuántas veces aparece el número 3 en la lista 'numeros'.
Imprime el resultado.
"""

cantidad = numeros.count(3)
print("El número 3 aparece", cantidad, "veces.")

# Ejercicio 8
"""
Crea una lista anidada con datos de 3 estudiantes: nombre, estatura y peso.
Llama a esta lista 'estudiantes'. Luego imprime la estatura del segundo estudiante.
"""

estudiantes = [["Laura", 1.65, 60], ["Pedro", 1.80, 75], ["Sofía", 1.70, 68]]
print("Estatura de Pedro:", estudiantes[1][1])

# Ejercicio 9
"""
Usa el método .pop() para eliminar el último elemento de la lista 'numeros'.
Imprime la lista resultante.
"""

numeros.pop()
print("Lista después de eliminar el último elemento:", numeros)

# Ejercicio 10
"""
Ordena alfabéticamente la lista 'dias'.
Imprime la lista ordenada.
"""

dias.sort()
print("Días ordenados alfabéticamente:", dias)
# Version Aitor

# Ejercicios Ficheros

"""Recuerda marcar como directorio de trabajo el script donde estés ejecutando el fichero. 
También puedes crear una subcarpeta “archivos” donde meter todos los ficheros, para ello 
puedes usar rutas relativas: "./archivos/nombre_archivo.txt"
"""

# Ejercicio 1: Leer un fichero de texto
"""
Objetivo: Crea un script que lea el contenido de un fichero llamado poema.txt y muestre su contenido en la consola.
Abre el fichero en modo lectura ("r").
Lee todo el contenido del fichero.
Muestra el contenido en pantalla.
Pistas:
Usa la función open() para abrir el fichero.
Usa el método .read() para leer todo el contenido de una sola vez."""

fichero = open("datos/poema.txt", "r", encoding="utf-8")
contenido = fichero.read()
fichero.close() # Cierra el fichero manualmente
print(contenido)

# Alternativa usando with, que cierra el fichero automáticamente
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
    print(contenido)
    # Cierra el fichero automáticamente al salir del bloque with

#Ejercicio 2: Escribir en un fichero de texto
"""
Objetivo: Crea un script que escriba un mensaje en un fichero llamado notas.txt.
Abre el fichero en modo escritura ("w").
Si el fichero no existe, debe crearse automáticamente.
Escribe en el fichero: "Esta es mi primera nota en este archivo."
Pistas:
Recuerda que el modo "w" sobrescribe el contenido si el fichero ya existe.
Usa el método .write() para escribir en el fichero.
"""
with open("datos/notas.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Esta es mi primera nota en este archivo.\n")   


# Ejercicio 3: Añadir contenido a un fichero
"""
Objetivo: Modifica el script del Ejercicio 2 para que no sobrescriba el contenido, 
sino que añada texto al final del fichero.
Abre el fichero notas.txt en modo añadir ("a").
Añade el siguiente mensaje: "Esta es otra línea añadida al archivo."
Pistas:
Usa el modo "a" para añadir contenido al final del fichero sin eliminar lo anterior.
"""
with open("datos/notas.txt", "a", encoding="utf-8") as fichero:
    fichero.write("Esta es otra línea añadida al archivo.\n")

"""
Ejercicio 4: Leer líneas de un fichero
Objetivo: Crea un script que lea y muestre cada línea de un fichero de texto, línea por línea.
Usa el fichero poema.txt del Ejercicio 1.
Abre el fichero en modo lectura.
Lee el contenido línea por línea y muestra cada línea por separado.
Pistas:
Usa un bucle for para recorrer cada línea del fichero.
"""
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea.strip())  # strip() elimina los saltos de línea adicionales

# Alternativamente, podrías usar readlines() y un bucle for:
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    for linea in lineas:
        print(linea.strip())  # strip() elimina los saltos de línea adicionales


"""
Ejercicio 5: Manejo de excepciones al leer un fichero
Objetivo: Crea un script que intente leer un fichero llamado archivo_inexistente.txt y capture el error si el fichero no existe.
Usa un bloque try-except para manejar el error FileNotFoundError.
Si el fichero no se encuentra, muestra el mensaje "Error: El archivo no existe.".
"""
try:
    with open("datos/archivo_inexistente.txt", "r", encoding="utf-8") as fichero:
        contenido = fichero.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")



"""

Ejercicio 6: Contar líneas y palabras en un fichero
Objetivo: Crea un script que cuente el número de líneas y el número total de palabras en un fichero llamado texto.txt.
Abre el fichero en modo lectura.
Recorre cada línea del fichero, contando el número de líneas.
Para cada línea, cuenta cuántas palabras contiene y suma el total de palabras.
Muestra el número total de líneas y el número total de palabras.
Pistas:
Usa el método .split() para dividir una línea en palabras.
Utiliza un contador para sumar las palabras.
"""
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    num_lineas = len(lineas)
    num_palabras = 0
    for linea in lineas:
        num_palabras += len(linea.split())
    print(f"Número total de líneas: {num_lineas}")
    print(f"Número total de palabras: {num_palabras}")  


"""
Ejercicio 7: Leer un fichero y buscar una palabra
Objetivo: Crea un script que lea un fichero llamado libro.txt y busque una palabra específica introducida por el usuario.
Solicita al usuario que introduzca la palabra a buscar.
Abre el fichero y recorre su contenido.
Muestra cuántas veces aparece la palabra en el fichero.
Pistas:
Usa el método .count() para contar las apariciones de la palabra en cada línea.

"""
def buscar_palabra_en_fichero(fichero, palabra):
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        num_apariciones = 0
        for indice, linea in enumerate(lineas):
            lista_palabras = linea.split()
            veces = lista_palabras.count(palabra)
            print(indice, veces)
            num_apariciones += veces
    return num_apariciones

buscar_palabra_en_fichero("datos/poema.txt", "la")


# Ejercicio 8: Leer las lineas del poema y guardarlas en in pickle
"""
Objetivo: Crea un script que lea las líneas de un fichero llamado poema.txt 
y las guarde en un fichero binario usando pickle.
"""

import pickle

with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()

with open("datos/poema.pickle", "wb") as fichero_binario:
    pickle.dump(lineas, fichero_binario)


with open("datos/poema.pickle", "rb") as fichero_binario:
    lineas_recuperadas = pickle.load(fichero_binario)
print(lineas_recuperadas)
type(lineas_recuperadas)
lineas_recuperadas.append("Linea nueva\n")