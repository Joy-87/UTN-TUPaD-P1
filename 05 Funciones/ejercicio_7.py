def operaciones_basicas(a, b):
    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = None 
    return (suma, resta, multiplicacion, division)

try:
    num1_ops = float(input("Ingresa el primer número para operaciones: "))
    num2_ops = float(input("Ingresa el segundo número para operaciones: "))
    
    resultados_ops = operaciones_basicas(num1_ops, num2_ops)
    
    print(f"Suma: {resultados_ops[0]}")
    print(f"Resta: {resultados_ops[1]}")
    print(f"Multiplicación: {resultados_ops[2]}")
    if resultados_ops[3] is not None:
        print(f"División: {resultados_ops[3]:.2f}") 
    else:
        print("División: No se puede dividir por cero.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos.")
