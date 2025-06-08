def fibonacci_recursivo(posicion):
    
    if posicion <= 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)


def mostrar_serie_fibonacci():
    
    while True:
        try:
            posicion_usuario = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
            if posicion_usuario < 0:
                print("Por favor, ingrese una posición no negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    print(f"\nSerie de Fibonacci hasta la posición {posicion_usuario}:")
    for i in range(posicion_usuario + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")

# Ejemplo de uso:
if __name__ == "__main__":
    mostrar_serie_fibonacci()