def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        if base == 0:
            raise ValueError ("Indefinido: 0 elevado a un exponente negativo")
        return 1 / potencia_recursiva(base, -exponente )
    else:
        return base *potencia_recursiva(base, exponente -1)


def probar_potencia_recursiva():
    """
    Algoritmo general para probar la función potencia_recursiva.
    """
    print("--- Pruebas de la Función potencia_recursiva ---")

    # Caso 1: Exponente positivo
    base1 = 2
    exponente1 = 3
    resultado1 = potencia_recursiva(base1, exponente1)
    print(f"La potencia de {base1} elevado a {exponente1} es: {resultado1} (Esperado: 8)")
    assert resultado1 == 8

    # Caso 2: Exponente cero
    base2 = 5
    exponente2 = 0
    resultado2 = potencia_recursiva(base2, exponente2)
    print(f"La potencia de {base2} elevado a {exponente2} es: {resultado2} (Esperado: 1)")
    assert resultado2 == 1

    # Caso 3: Exponente negativo
    base3 = 2
    exponente3 = -2
    resultado3 = potencia_recursiva(base3, exponente3)
    print(f"La potencia de {base3} elevado a {exponente3} es: {resultado3} (Esperado: 0.25)")
    assert resultado3 == 0.25

    # Caso 4: Base negativa y exponente par
    base4 = -3
    exponente4 = 2
    resultado4 = potencia_recursiva(base4, exponente4)
    print(f"La potencia de {base4} elevado a {exponente4} es: {resultado4} (Esperado: 9)")
    assert resultado4 == 9

    # Caso 5: Base negativa y exponente impar
    base5 = -2
    exponente5 = 3
    resultado5 = potencia_recursiva(base5, exponente5)
    print(f"La potencia de {base5} elevado a {exponente5} es: {resultado5} (Esperado: -8)")
    assert resultado5 == -8

    # Caso 6: Base 1
    base6 = 1
    exponente6 = 100
    resultado6 = potencia_recursiva(base6, exponente6)
    print(f"La potencia de {base6} elevado a {exponente6} es: {resultado6} (Esperado: 1)")
    assert resultado6 == 1

    # Caso 7: Base 0 y exponente positivo
    base7 = 0
    exponente7 = 5
    resultado7 = potencia_recursiva(base7, exponente7)
    print(f"La potencia de {base7} elevado a {exponente7} es: {resultado7} (Esperado: 0)")
    assert resultado7 == 0

    # Caso 8: Prueba de error (0 elevado a exponente negativo)
    base8 = 0
    exponente8 = -3
    try:
        potencia_recursiva(base8, exponente8)
        print(f"Error: 0 elevado a {exponente8} debería haber lanzado un error.")
    except ValueError as e:
        print(f"Manejo de error correcto: {base8} elevado a {exponente8} resultó en un error: {e}")

    print("\nTodas las pruebas se completaron.")


# Ejecutar el algoritmo de prueba
probar_potencia_recursiva()