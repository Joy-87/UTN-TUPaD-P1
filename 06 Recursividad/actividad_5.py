def es_palindromo(palabra):
    """
    Verifica si una cadena de texto es un palíndromo de forma recursiva.
    La cadena no debe contener espacios ni tildes.

    Args:
        palabra (str): La cadena de texto a verificar.

    Returns:
        bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def probar_es_palindromo():
    """
    Algoritmo general para probar la función es_palindromo con entrada de usuario.
    """
    palabra_usuario = input("Ingrese una palabra (sin espacios ni tildes): ")

    
    es_o_no = es_palindromo(palabra_usuario)

   
    if es_o_no:
        print(f"¡Sí! '{palabra_usuario}' ES un palíndromo.")
    else:
        print(f"No. '{palabra_usuario}' NO es un palíndromo.")
  
probar_es_palindromo()