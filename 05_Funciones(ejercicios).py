"""
Spyder Editor

This is a temporary script file.
"""

# 1. Calculadora Simple:
"""
Crea una función que pueda realizar operaciones básicas como suma, resta, 
multiplicación y división. 
Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.


Utiliza funciones separadas para cada operación.
"""
def operacion_suma(a, b):
    return a + b    

def operacion_resta(a, b):
    return a - b

def operacion_multiplicacion(a, b):
    return a * b

def operacion_division(a, b):
    return a / b                
def calculadora(operacion, a, b):
    if operacion == 1:
        return operacion_suma(a, b)
    elif operacion == 2:
        return operacion_resta(a, b)
    elif operacion == 3:
        return operacion_multiplicacion(a, b)
    elif operacion == 4:
        return operacion_division(a, b)
    else:
        return "Operación no válida"    
print("""
    Elige la operación a realizar:
      1 = Suma
      2 = Resta
      3 = Multiplicación
      4 = División
""")
operacion = int(input("Elige la operación: "))
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print(calculadora(operacion, a, b))

# opcion Aitor con diccionario
print("""
    Elige la operación a realizar:
      1 = Suma
      2 = Resta
      3 = Multiplicación
      4 = División
""")

def pedir_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

def sumar():
    print("suma")
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 + num2}")

def restar():
    print("suma")
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 - num2}")

def multiplicar():
    print("suma")
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 * num2}")

def dividir():
    print("suma")
    num1, num2 = pedir_numeros()
    if num2 == 0:
        print("No se puede dividir por cero")
        return
    else:
        print(f"El resultado es: {num1 / num2}")

def salir():
    pass

def calculadora():
    while True:
        print("""
            Elige la operación a realizar:
            1 = Suma
            2 = Resta
            3 = Multiplicación
            4 = División
            5 = Salir
        """)
        operaciones = {"1": sumar, "2": restar, "3": multiplicar, "4": dividir , "5": salir}
        opcion = input("Ingrese la opción: ")
        if opcion not in operaciones.keys():
            print("Opción no válida")
            continue
        if opcion =="5":
            break
        else:
            operacion = operaciones[opcion]
            operacion()

calculadora()


# 2. Número Primo:
"""
Escribe una función que determine si un número dado es primo o no. 
Pedirá al usuario que ingrese un número y muestra un mensaje 
indicando si es primo o no.
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    numero = int(input("Introduce un número para comprobar si es primo: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
except ValueError:
    print("Por favor, introduce un número entero válido.")

#version Aitor
def es_primo(numero):
    if numero == 1:
        return False
    factor = 2
    while factor < numero:
        if numero % factor == 0:
            print(f"{numero} no es primo", factor)
            return False
        factor += 1
    return True

def verifica_primo():
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(f"{numero} es primo")

verifica_primo()




# 3. Cálculo del Área:
"""
Implementa funciones para calcular el área de diferentes formas geométricas 
como círculo, cuadrado y triángulo. Pide al usuario que elija la forma y 
luego ingrese los valores necesarios.
"""
print("""
Opcion
    1 : Circulo
    2 : Cuadrado
    3 : Triángulo

""")
from  math import pi 

def area_circulo(radio):
    return pi * radio ** 2

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

opcion = int(input("Elige la figura: "))
if opcion == 1:
    radio = float(input("Ingresa el radio del círculo: "))
    print(f"El área del círculo es: {area_circulo(radio)}")
elif opcion == 2:    
    lado = float(input("Ingresa el lado del cuadrado: "))
    print(f"El área del cuadrado es: {area_cuadrado(lado)}")
elif opcion == 3:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    print(f"El área del triángulo es: {area_triangulo(base, altura)}")    
else:
    print("Opción no válida. Por favor, elige una figura válida.")  

 # Version Aitor calculo de area
from math import pi as PI


def area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = PI * radio ** 2
    print(f"El área del círculo es: {area}")

def area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es: {area}")

def area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")  

def calculadora_areas():
    while True:
        print("""
            Opcion
                1 : Circulo
                2 : Cuadrado
                3 : Triángulo
                q : Salir
        """)
        opcion = input("Ingrese la opción deseada: ")
        match opcion:
            case "1":
                area_circulo()
            case "2":
                area_cuadrado()
            case "3":
                area_triangulo()
            case "q":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")
calculadora_areas()




# 4. Inversión de Cadena:
"""
Crea una función que tome una cadena como entrada y devuelva la cadena invertida. 
Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".
"""



def invertir_cadena(cadena):
    return cadena[::-1]

texto = input("Introduce una cadena para invertir: ")
print("Cadena invertida:", invertir_cadena(texto))

# Version Aitor

def invertir_cadena():
    cadena = input("Ingrese una cadena: ")
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    print(f"La cadena invertida es: {cadena_invertida}")    



# 5. Contador de Palabras:
"""
Desarrolla una función que cuente el número de palabras en una oración. 
Pide al usuario que ingrese una oración y muestra el resultado.
"""

def contar_palabras(oracion):
    return len(oracion.split())

oracion = input("Introduce una oración: ")
print("Número de palabras:", contar_palabras(oracion))

# Version Aitor
def cuenta_palabras(frase):
    contador = 0
    for letra in frase:
        if letra == " ":
            contador += 1
    return contador + 1
def pide_palabras2(frase):
    frase = input("Ingrese una frase: ")
    print(f"La frase tiene {cuenta_palabras(frase)} palabras")
pide_palabras2("frase")




# 6. Fibonacci:
"""
Implementa una función para generar los primeros n números de la 
secuencia de Fibonacci. Pide al usuario que ingrese el valor de n.
"""
def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[i-1] + secuencia[i-2]
        secuencia.append(siguiente)
    return secuencia[:n]

n = int(input("Ingresa el valor de n: "))
print("Los primeros", n, "números de Fibonacci son:", fibonacci(n))



# 7. Ordenar Lista:
"""
Escribe una función que ordene una lista de números de manera ascendente 
o descendente según la elección del usuario.
"""
lista_numeros = [5, 2, 9, 1, 5, 6]
def ordenar_lista(lista, orden='ascendente'):
    if orden == 'ascendente':
        return sorted(lista)
    elif orden == 'descendente':
        return sorted(lista, reverse=True)
    else:
        return "Orden no válido. Usa 'ascendente' o 'descendente'."

orden = input("Ingresa 'ascendente' o 'descendente': ")
print("Lista ordenada:", ordenar_lista(lista_numeros, orden))   



# 8. Factorial:
"""
Crea una función para calcular el factorial de un número. 
Pide al usuario que ingrese un número y muestra el resultado.
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Ingresa un número: "))
print("El factorial de", n, "es:", factorial(n))


# 9. Conversión de Temperatura:
"""
Implementa funciones para convertir entre Celsius y Fahrenheit. 
Pide al usuario que ingrese la temperatura y la unidad, y luego 
realiza la conversión.
"""
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input("Ingresa la temperatura: "))
unidad = input("Ingresa 'C' para Celsius o 'F' para Fahrenheit: ")

if unidad.upper() == 'C':
    print(f"{temperatura}°C es igual a {celsius_a_fahrenheit(temperatura)}°F")
elif unidad.upper() == 'F':
    print(f"{temperatura}°F es igual a {fahrenheit_a_celsius(temperatura)}°C")
else:
    print("Unidad no válida. Por favor, ingresa 'C' o 'F'.")    

# 10. Juego de Adivinanzas:
"""
Desarrolla un juego simple en el que el programa elige un número aleatorio 
y el jugador tiene que adivinarlo. 
Proporciona pistas sobre si el número es mayor o menor. 
Utiliza funciones para organizar el código.
"""
import random
def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0        
    while True:
        intento = int(input("Adivina el número entre 1 y 100: "))
        intentos += 1
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()
