#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:45:24 2023

@author: Aitor Donado
"""

# 1. Crear una lista con 10 elementos numéricos.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2. Comprobar si el tercer elemento es mayor que el séptimo y crear una frase que
# muestre por escrito si el número es mayor o menor y el valor que toma el tercer elemento.
if numeros[2] > numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es mayor que el séptimo elemento ({numeros[6]}).")


# 3. Invertir el orden de la lista y realizar la misma comprobación.
numeros.reverse()
if numeros[2] > numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es mayor que el séptimo elemento ({numeros[6]}).")


# 4. Añadir la posibilidad de que sea igual.
if numeros[2] == numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es igual que el séptimo elemento ({numeros[6]}).")


# 5. Transformar el séptimo número para que se satisfaga la igualdad.
numeros[6] = numeros[2]


# 6. Realizar la comprobación.
if numeros[2] == numeros[6]:
    print(f"El tercer elemento ({numeros[2]}) es igual que el séptimo elemento ({numeros[6]}).")

