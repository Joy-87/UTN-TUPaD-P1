
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#     - Las capitales sean las claves.
#     - Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín"
}

invertido = {}

# Iterar sobre los pares clave-valor del diccionario original
for pais, capital in original.items():
    invertido[capital] = pais # Asignar la capital como clave y el país como valor en el nuevo diccionario

print("Diccionario original (País: Capital):")
print(original)

print("\nDiccionario invertido (Capital: País):")
print(invertido)