
# Inicializar un diccionario vacío para los contactos
contactos = {}

print("--- Carga de 5 contactos ---")
# Permitir al usuario cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = numero
    print(f"Contacto '{nombre}' agregado.")

print("\n--- Consulta de números telefónicos ---")
# Pedir un nombre y mostrar el número asociado, si existe
nombre_buscar = input("Ingrese el nombre del contacto que desea buscar: ")

if nombre_buscar in contactos:
    print(f"El número de teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"El contacto '{nombre_buscar}' no se encuentra en la agenda.")

print("\n--- Contactos guardados ---")
print(contactos)