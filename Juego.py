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

# version  Aitor
from random import randint

def adivina_numero():
    numero_aleatorio = randint(0, 100)

    # Pedir al usuario que adivine el número
    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento == numero_aleatorio:
            print("¡Correcto! Adivinaste el número.")
            break
        elif intento < numero_aleatorio:
            print("El número a adivinar es mayor que", intento)
        else:
            print("El número a adivinar es menor que", intento)