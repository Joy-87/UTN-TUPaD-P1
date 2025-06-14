
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#    Luego, mostrá el promedio de cada alumno.

alumnos = {}

print("--- Ingreso de datos de 3 alumnos ---")
for i in range(3):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    notas = []
    print(f"Ingrese 3 notas para {nombre_alumno}:")
    for j in range(3):
        while True: # Bucle para asegurar que se ingresa un número válido
            try:
                nota = float(input(f"  Nota {j+1}: "))
                notas.append(nota)
                break # Salir del bucle si la nota es válida
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para la nota.")
    
    # Convertir la lista de notas a una tupla
    alumnos[nombre_alumno] = tuple(notas)
    print(f"Notas de {nombre_alumno} guardadas: {alumnos[nombre_alumno]}")

print("\n--- Promedio de cada alumno ---")
for nombre, notas_tuple in alumnos.items():
    if notas_tuple: # Asegurarse de que haya notas para calcular el promedio
        promedio = sum(notas_tuple) / len(notas_tuple)
        print(f"El promedio de {nombre} es: {promedio:.2f}") # Formatear a 2 decimales
    else:
        print(f"No hay notas para {nombre}.")

print("\nDiccionario de alumnos completo:")
print(alumnos)