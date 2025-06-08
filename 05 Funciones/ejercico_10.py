def calcular_promedio(a, b, c):
    
    return (a + b + c) / 3

try:
    num1_prom = float(input("Ingresa el primer número para el promedio: "))
    num2_prom = float(input("Ingresa el segundo número para el promedio: "))
    num3_prom = float(input("Ingresa el tercer número para el promedio: "))

    promedio = calcular_promedio(num1_prom, num2_prom, num3_prom)
    print(f"El promedio de los tres números es: {promedio:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos.")
