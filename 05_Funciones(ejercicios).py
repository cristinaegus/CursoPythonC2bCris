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

numero = int(input("Introduce un número para comprobar si es primo: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")






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
def area_circulo(radio):
    return 3.14 * radio ** 2

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




# 4. Inversión de Cadena:
"""
Crea una función que tome una cadena como entrada y devuelva la cadena invertida. 
Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".
"""



def invertir_cadena(cadena):
    return cadena[::-1]

texto = input("Introduce una cadena para invertir: ")
print("Cadena invertida:", invertir_cadena(texto))






# 5. Contador de Palabras:
"""
Desarrolla una función que cuente el número de palabras en una oración. 
Pide al usuario que ingrese una oración y muestra el resultado.
"""

def contar_palabras(oracion):
    return len(oracion.split())

oracion = input("Introduce una oración: ")
print("Número de palabras:", contar_palabras(oracion))




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


# 8. Factorial:
"""
Crea una función para calcular el factorial de un número. 
Pide al usuario que ingrese un número y muestra el resultado.
"""

# 9. Conversión de Temperatura:
"""
Implementa funciones para convertir entre Celsius y Fahrenheit. 
Pide al usuario que ingrese la temperatura y la unidad, y luego 
realiza la conversión.
"""

# 10. Juego de Adivinanzas:
"""
Desarrolla un juego simple en el que el programa elige un número aleatorio 
y el jugador tiene que adivinarlo. 
Proporciona pistas sobre si el número es mayor o menor. 
Utiliza funciones para organizar el código.
"""