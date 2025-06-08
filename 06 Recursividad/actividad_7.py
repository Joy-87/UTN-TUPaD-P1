def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide
    de forma recursiva. En el nivel más bajo se colocan 'n' bloques,
    en el siguiente 'n-1', y así sucesivamente hasta llegar a 1.

    Args:
        n (int): El número de bloques en el nivel más bajo (debe ser un entero positivo).

    Returns:
        int: El total de bloques para construir la pirámide.

    Raises:
        ValueError: Si 'n' no es un entero positivo.
    """
    # Validación de entrada para asegurar que n sea un entero positivo
    if not isinstance(n, int) or n <= 0:
        raise ValueError("El número de bloques en el nivel más bajo (n) debe ser un entero positivo.")

    # Caso Base: Si n es 1, solo hay un bloque en el nivel más bajo.
    if n == 1:
        return 1
    else:
        
        return n + contar_bloques(n - 1)
def probar_contar_bloques():
    """
    Solicita al usuario el número de bloques en el nivel más bajo de la pirámide,
    calcula el total de bloques con la función recursiva contar_bloques,
    y muestra el resultado.
    """
    print("--- Calculadora de Bloques de Pirámide (Recursiva) ---")

    while True:
        try:
            entrada_usuario = input("Ingrese el número de bloques en el nivel más bajo (n) (o 'salir' para terminar): ")
            
            if entrada_usuario.lower() == 'salir':
                print("¡Gracias por usar la calculadora!")
                break # Sale del bucle
            
            n_bloques = int(entrada_usuario)
            
            # Llamamos a la función contar_bloques con el número ingresado
            total_bloques = contar_bloques(n_bloques)
            
            print(f"Para una pirámide con {n_bloques} bloques en la base, se necesitan un total de {total_bloques} bloques.")
        
        except ValueError as e:
            # Capturamos errores de la función contar_bloques (si n es no positivo)
            # o si la entrada del usuario no es un número entero válido.
            print(f"Error: {e}. Por favor, ingrese un número entero positivo válido.")
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el algoritmo de prueba
probar_contar_bloques()    