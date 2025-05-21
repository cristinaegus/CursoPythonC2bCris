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
Extrae los tres primeros elementos de la lista 'dias' y guárdalos en una nueva lista llamada 'inicio_semana'.
Imprime esa nueva lista.
"""
inicio_semana = dias[:3]
print("Inicio de la semana:", inicio_semana)

# Ejercicio 4
"""
Desempaqueta la lista 'dias' en tres variables"""
a,b,c = inicio_semana
a,b,c,_,_,_= dias
print("Primer día:", a)
print("Segundo día:", b)    
print("Tercer día:", c)


# Ejercicio 5
"""
Crea una lista llamada 'numeros' con los números del 1 al 5.
Agrega el número 6 al final de la lista.
Luego imprime la longitud de la lista.
"""
numeros = [1, 2, 3, 4, 5]
list(range(1,6))
numeros.append(6)
print, len(numeros)

# Ejercicio 6
"""
Concatena la lista [8, 9, 10] a la lista 'numeros'.
Imprime la nueva lista.
"""
lista_nueva = [8, 9, 10]
numeros + lista_nueva
numeros.extend(lista_nueva)
print(numeros)



# Ejercicio 7
"""
Cuenta cuántas veces aparece el número 3 en la lista 'numeros'.
Imprime el resultado.
"""
numeros .count(3)
print("El número 3 aparece", numeros.count(3), "veces en la lista.")

# Ejercicio 8
"""
Crea una lista anidada con datos de 3 estudiantes: nombre, estatura y peso.
Llama a esta lista 'estudiantes'. Luego imprime la estatura del segundo estudiante.
"""

lista_estudiantes = [["Laura", 1.65, 60], ["Pedro", 1.80, 75], ["Sofía", 1.70, 68]]
print("Estatura del segundo estudiante:", lista_estudiantes[1][1])
# se puede hacer tambien con un diccionario
estudiante1 = {"nombre": "Laura", "estatura": 1.65, "peso": 60}
estudiante2 = {"nombre": "Pedro", "estatura": 1.80, "peso": 75}
estudiante3 = {"nombre": "Sofía", "estatura": 1.70, "peso": 68} 
print("Estatura del segundo estudiante:", estudiante2["estatura"])

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
print("Lista de días ordenada alfabéticamente:", dias)
