def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def calcular_factoriales_hasta_n():
    while True: # Añadido un bucle para validación de entrada
        try:
            num_usuario = int(input("Ingrese un número entero positivo: "))
            if num_usuario < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                break # Sale del bucle si la entrada es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    print(f"\nFactoriales hasta {num_usuario}:") # Mensaje para claridad
    for i in range(1, num_usuario + 1):
        print(f"El factorial de {i} es: {factorial_recursivo(i)}")

if __name__ == "__main__":
    calcular_factoriales_hasta_n()