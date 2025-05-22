def area (radio):
 return 3.14 * radio ** 2
def perimetro (radio):
 return 2 * 3.14 * radio
if __name__ == "__main__":
    print("Ejecutando el módulo como programa principal")   
    print("El área de un círculo de radio 5 es:", area(5))
    print("El perímetro de un círculo de radio 5 es:", perimetro(5))
print(area(25))
print(perimetro(35))
