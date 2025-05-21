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
        print("El número es par")
    else:
        print("El número es impar") 
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


# 3. Tabla de multiplicar:
"""
Pide al usuario que ingrese un número y luego muestra la tabla de 
multiplicar de ese número del 1 al 10 utilizando un bucle for.
"""
input_num = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = input_num * i
    print(f"{input_num} x {i} = {resultado}")
    


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

# 5. Adivina el número:
"""
Crea un juego en el que el programa genera un número aleatorio y el 
usuario tiene que adivinarlo. Utiliza un bucle while para que el usuario 
pueda seguir intentando hasta que adivine el número. Proporciona pistas 
para indicar si el número a adivinar es mayor o menor que el intento del 
usuario.
"""
from random import randint

randint(0, 100)