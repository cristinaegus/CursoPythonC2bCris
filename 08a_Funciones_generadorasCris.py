# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:34:31 2023

@author: Aitor Donado
"""

# En este script vamos a utilizar time para simular la 
# ejecución de tareas lentas

import time
"""
Las funciones, como hemos visto hasta ahora devuelven un valor con return,
la preculiaridad de los generadores es que van cediendo valores 
sobre la marcha, en tiempo de ejecución.
"""

def es_primo(numero):
    """Función que devuelve True si el número introducido es primo"""
    es_primo = True
    factor = 2
    while factor < numero:
        if numero % factor == 0:
            es_primo = False
            return es_primo
        factor += 1
    return es_primo

"""
Supongamos que queremos una gran cantidad de números primos.
Si creamos una función que nos devuelva una lista de números primos
tendremos que esperar a que calcule la lista completa para 
empezar a utilizarlos en el uso que les queramos dar.

"""
def crea_lista_primos(n,m):
    lista_numeros_primos =  []
    for numero in range(n, m+1):
        # Simulamos la ejecución de código lento con una parada de 1 segundo
        time.sleep(1)
        if es_primo(numero):
            lista_numeros_primos.append(numero)
    return lista_numeros_primos

crea_lista_primos(5,15)

def primos(n, m):
    for numero in range(n, m+1):
        # Simulamos la ejecución de código lento con una parada de 1 segundo
        time.sleep(1)
        if es_primo(numero):
            yield numero

"""
La función range(0,11), empieza cediendo el 0, 
    luego se procesa el for comprobando si es primo y lo añade a la lista, 
    en la siguiente iteración se cede el 1, en la siguiente se cede el 2, etc.

Con esto se logra 
    ocupar el mínimo de espacio en la memoria al poder generar listas de 
    millones de elementos sin necesidad de almacenarlos previamente.
"""

generador_de_primos = primos(5,45)
# Cuando creamos el generador aún no se ha ejecutado la instrucción
next(generador_de_primos)
# Al pedir "next" se ejecuta la instrucción y nos va devolviendo los valores
# según se crean
next(generador_de_primos)
# Podríamos utilizar ya el contenido creado
next(generador_de_primos)

for primo in generador_de_primos:
    # Al llamar a la función en cada tacada del bucle 
    # se genera el valor primo y se imprime
    print(primo)

# El for ha continuado a partir del siguiente valor que obtuvimos con next

# El generador ahora está agotado
next(generador_de_primos)

generador_de_primos = primos(5,20)

# Si guardo el generador en una lista, tengo que esperar a que se ejecute toda la lista
# por tanto, pierdo la ventaja de usar el generador.
lista_primos = list(generador_de_primos)
print(lista_primos)

for numero in primos(5, 20):
    print(numero)

for numero in range(5, 20):
    print(numero)

# Es posible convertir una lista en un iterable
lista = [1, 2, 54, 3, 23, 6, "Hola", 6, 69, 6, 78, 5]
lista_iterable = iter(lista)

next(lista_iterable)
next(lista_iterable)
next(lista_iterable)

# List Comprenhension
# Lista de primos que terminan en 7

def primos(n, m):
    for numero in range(n, m+1):
        # Simulamos la ejecución de código lento con una parada de 1 segundo
        if es_primo(numero):
            yield numero

generador_de_primos = primos(0,100)

[numero for numero in generador_de_primos if str(numero)[-1] == "7"]

#lista_primos = []
#for numero in generador_de_primos: compreension 


#___________#
# Ejercicio #
#-----------#
# Crear un generador que busca en un archivo líneas que contengan una subcadena coincidente:
# Usar ese generador para leer El Quijote, cuando el generador encuentre la palabra Quijote,
# imprime la línea y para hasta que el usuario le da a "intro" (con un input vacío)
generador_quijote = open("../CursoPythonC2bCris/datos/quijote.txt", "r", encoding="utf-8")
def buscar_subcadena_en_archivo(archivo, subcadena):
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if subcadena in linea:
                yield linea.strip()
                input("Presiona Enter para continuar...")
                # Si el usuario presiona Enter, se detiene el generador
                break    
buscar_subcadena_en_archivo("../CursoPythonC2bCris/datos/quijote.txt", "Quijote")
print("Fin del generador")


#__________#
# Solución #
#----------#

def buscar_lineas_con_subcadena(archivo_quijote, subcadena):
    with open(archivo_quijote, "r", encoding="utf-8") as f:
        for linea in f:
            if subcadena in linea:
                yield linea.strip()

# Uso del generador para buscar "Quijote" en el archivo
archivo_quijote = "../CursoPythonC2bCris/datos/quijote.txt"
subcadena = "Quijote"
generador_quijote = buscar_lineas_con_subcadena(archivo_quijote, subcadena)
# Imprime cada línea que contiene la subcadena y espera a que el usuario presione Enter
for linea in buscar_lineas_con_subcadena(archivo_quijote, subcadena):
    print(linea, end="")
    # Espera a que el usuario presione Enter para continuar
    input("Presiona Enter para continuar...")









#Version Aitor
with open("../CursoPythonC2bCris/datos/quijote.txt", "r", encoding="utf-8") as archivo:
       linea = archivo.readlines(1)  # Aquí puedes añadir el código que desees ejecutar con el archivo abierto
       linea = archivo.readlines(2)     
         

