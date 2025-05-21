#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:48:07 2023

@author: laptop
"""

# 1. Contador de números pares e impares:
"""
Escribe un programa que utilice un bucle for o while para contar y mostrar 
la cantidad de números pares e impares en un rango específico, 
por ejemplo, del 1 al 100.
"""
lista = list(range(1, 101))
for elemento in lista:
    if elemento % 2 == 0:
        print(f"{elemento} El número es par")
    else:
        print(f"{elemento} El número es impar") 
# Alternativa que lo guarda en una lista cuando es par y en otra cuando es impar
lista = list(range(1, 101))
lista_pares = []
lista_impares = []
for elemento in lista:
    if elemento % 2 == 0:
        lista_pares.append(elemento)
    else:
        lista_impares.append(elemento)
print(lista_pares)
print(lista_impares)
        
# 2. Suma de números primos:
"""
Crea un programa que solicite al usuario un número y utilice un bucle 
while para sumar todos los números primos menores o iguales al número 
ingresado.
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#alternativa Cris este esta bien
numero = int(input("Introduce un número: "))
# while numero < 0:
#     if numero % factor == 0:
#         print(f "{numero} no es primo,.factor")
#         break
factor = 2
es_primo = True
while factor < numero:
    if numero % factor == 0:
        es_primo = False
        break
    factor += 1
lista_primos = []

candidato_a_primo = 2  # Inicializamos el primer candidato a primo

while candidato_a_primo < numero:
    es_primo = True
    for factor in range(2, int(candidato_a_primo ** 0.5) + 1):
        if candidato_a_primo % factor == 0:
            es_primo = False
            break
    if es_primo:
        lista_primos.append(candidato_a_primo)
    candidato_a_primo += 1
        
    

# 3. Tabla de multiplicar:
"""
Pide al usuario que ingrese un número y luego muestra la tabla de 
multiplicar de ese número del 1 al 10 utilizando un bucle for.
"""
input_num = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = input_num * i
    print(f"{input_num} x {i} = {resultado}")
  # Alternativa aitor esta bien  
input_num = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1,numero + 1):
   print(str(i) * i)


# 4. Generador de patrones:
"""
Escribe un programa que solicite al usuario un número y utilice 
un bucle for o while para generar patrones como el siguiente, donde 
el número ingresado determine la cantidad de filas:
"""
1
22
333
4444
55555
66666
num_filas = int(input("Introduce la cantidad de filas para el patrón: "))
for i in range(1, num_filas + 1):
    print(str(i) * i)

# 5. Adivina el número:Correcto
"""
Crea un juego en el que el programa genera un número aleatorio y el 
usuario tiene que adivinarlo. Utiliza un bucle while para que el usuario 
pueda seguir intentando hasta que adivine el número. Proporciona pistas 
para indicar si el número a adivinar es mayor o menor que el intento del 
usuario.
"""
from random import randint

numero_secreto = randint(0, 100)
intento = None

while intento != numero_secreto:
    intento = int(input("Adivina el número (entre 0 y 100): "))
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
