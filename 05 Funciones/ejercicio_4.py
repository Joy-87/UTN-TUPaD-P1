import math
def calcular_area_circulo(radio):
    
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
   
    return 2 * math.pi * radio


try:
    radio_usuario = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio_usuario)
    perimetro = calcular_perimetro_circulo(radio_usuario)
    print(f"El área del círculo es: {area:.2f}") # Formatear a 2 decimales
    print(f"El perímetro del círculo es: {perimetro:.2f}") # Formatear a 2 decimales
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para el radio.")
