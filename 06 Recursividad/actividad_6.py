
def suma_digitos(n):
    """
    Calcula la suma de los dígitos de un número entero positivo de forma recursiva.

    Args:
        n (int): El número entero positivo.

    Returns:
        int: La suma de sus dígitos.

    Raises:
        ValueError: Si el número no es un entero positivo o cero.
    """
    # Validación de entrada para asegurar que sea un entero no negativo
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero positivo o cero.")

    # Caso Base: Si el número es 0, la suma de sus dígitos es 0.
    if n == 0:
        return 0
    else:
        # Caso Recursivo:
        # Obtenemos el último dígito (resto de la división por 10)
        ultimo_digito = n % 10
        # Obtenemos el resto del número (cociente de la división entera por 10)
        numero_restante = n // 10
        
        # Sumamos el último dígito con la suma de los dígitos restantes (recursión)
        return ultimo_digito + suma_digitos(numero_restante)
def probar_suma_digitos_usuario():
    """
    Solicita un número al usuario, calcula la suma de sus dígitos
    usando la función recursiva suma_digitos, y muestra el resultado.
    """
    print("--- Calculadora de Suma de Dígitos (Recursiva) ---")

    while True:
        try:
            entrada_usuario = input("Ingrese un número entero positivo (o 'salir' para terminar): ")
            
            if entrada_usuario.lower() == 'salir':
                print("¡Adiós!")
                break # Sale del bucle
            
            numero = int(entrada_usuario)
            
            # Llamamos a la función suma_digitos con el número ingresado
            resultado_suma = suma_digitos(numero)
            
            print(f"La suma de los dígitos de {numero} es: {resultado_suma}")
        
        except ValueError as e:
            # Capturamos errores de la función suma_digitos (si el número es negativo)
            # o si la entrada del usuario no es un número válido.
            print(f"Error: {e}. Por favor, ingrese un número entero positivo válido.")
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el algoritmo para probar la función con entrada de usuario
probar_suma_digitos_usuario()    