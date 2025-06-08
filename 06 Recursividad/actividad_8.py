def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito específico dentro de un número entero positivo
    de forma recursiva.

    Args:
        numero (int): El número entero positivo a inspeccionar.
        digito (int): El dígito (entre 0 y 9) a contar.

    Returns:
        int: El número de veces que el dígito aparece en el número.

    Raises:
        ValueError: Si 'numero' no es un entero positivo o cero, o si 'digito' no es un dígito válido (0-9).
    """
    # 1. Validación de Entrada
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("El 'numero' debe ser un entero positivo o cero.")
    if not isinstance(digito, int) or not (0 <= digito <= 9):
        raise ValueError("El 'digito' debe ser un entero entre 0 y 9.")
   
    if numero == 0:
        return 1 if digito == 0 else 0
    
    conteo_actual = 1 if (numero % 10) == digito else 0
    
    return conteo_actual + contar_digito(numero // 10, digito)


def probar_contar_digito_completo():
    
    while True:
        try:
            entrada_numero = input("Ingrese el número (o 'salir' para terminar): ")
            if entrada_numero.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            numero = int(entrada_numero)

            entrada_digito = input("Ingrese el dígito a contar (0-9): ")
            digito = int(entrada_digito)
            
            total_apariciones = contar_digito(numero, digito)
            print(f"El dígito {digito} aparece {total_apariciones} veces en el número {numero}.")
        
        except ValueError as e:
            print(f"Error en la entrada o en la función: {e}. Asegúrese de ingresar números válidos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el algoritmo principal
probar_contar_digito_completo()