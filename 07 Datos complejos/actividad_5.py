
# 5) Solicita al usuario una frase e imprime:
#    - Las palabras únicas (usando un set).
#    - Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresa una frase: ").lower() # Convertir a minúsculas para tratar palabras iguales como la misma
palabras = frase.split() # Dividir la frase en una lista de palabras

# Eliminar signos de puntuación de las palabras (opcional, para una mejor cuenta)
# Puedes expandir esta lógica para manejar más signos de puntuación si es necesario
palabras_limpias = []
for palabra in palabras:
    palabra = palabra.strip('.,!?"\'') # Elimina algunos signos de puntuación del inicio y final
    if palabra: # Asegurarse de que la palabra no esté vacía después de limpiar
        palabras_limpias.append(palabra)

# 1. Palabras únicas (usando un set)
palabras_unicas = set(palabras_limpias)
print("\nPalabras únicas:", palabras_unicas)

# 2. Diccionario con la cantidad de veces que aparece cada palabra
conteo_palabras = {}
for palabra in palabras_limpias:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1 # Incrementa el contador o lo inicializa en 1

print("Recuento:", conteo_palabras)