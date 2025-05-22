def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y devuelve un saludo personalizado.
    Args:
        nombre (str): El nombre del usuario.
    Returns:
        str: Un saludo personalizado, por ejemplo, "Hola [nombre]!".
    """
    return f"¡Hola {nombre}!"

# Llamar a la función desde el programa principal

nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)
