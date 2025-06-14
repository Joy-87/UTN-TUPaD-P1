
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

# Datos de ejemplo (puedes modificarlos si quieres probar con otros estudiantes)
aprobados_parcial1 = {101, 105, 108, 112, 115, 120}
aprobados_parcial2 = {105, 110, 112, 118, 120, 125}

print("Estudiantes que aprobaron Parcial 1:", aprobados_parcial1)
print("Estudiantes que aprobaron Parcial 2:", aprobados_parcial2)

# a. Mostrar los que aprobaron ambos parciales (intersección)
aprobados_ambos = aprobados_parcial1.intersection(aprobados_parcial2)
print("\nEstudiantes que aprobaron ambos parciales:", aprobados_ambos)

# b. Mostrar los que aprobaron solo uno de los dos (diferencia simétrica)
aprobados_solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)

# c. Mostrar la lista total de estudiantes que aprobaron al menos un parcial (unión sin repetir)
total_aprobados = aprobados_parcial1.union(aprobados_parcial2)
print("Lista total de estudiantes que aprobaron al menos un parcial (sin repetir):", total_aprobados)