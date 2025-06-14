
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {}

# Añadir algunos eventos
agenda[(15, "09:00")] = "Reunión con el equipo de marketing"
agenda[(15, "14:30")] = "Entrevista de trabajo"
agenda[(16, "10:00")] = "Cita con el dentista"
agenda[(17, "18:00")] = "Clase de yoga"

print("--- Mi Agenda ---")
# Mostrar los eventos en la agenda
if agenda:
    # Ordenar los eventos por día y luego por hora para una mejor visualización
    eventos_ordenados = sorted(agenda.items())
    for (dia, hora), evento in eventos_ordenados:
        print(f"Día {dia} a las {hora}: {evento}")
else:
    print("La agenda está vacía.")

# Consultar un evento específico
dia_consulta = 15
hora_consulta = "09:00"
clave_consulta = (dia_consulta, hora_consulta)

print(f"\nConsultando evento para el día {dia_consulta} a las {hora_consulta}:")
if clave_consulta in agenda:
    print(f"Evento: {agenda[clave_consulta]}")
else:
    print("No hay eventos programados para esta fecha y hora.")

# Intentar agregar un evento que sobrescribe uno existente
agenda[(15, "09:00")] = "Reunión de planificación de proyecto (ACTUALIZADO)"
print("\nAgenda después de actualizar un evento:")
eventos_ordenados = sorted(agenda.items())
for (dia, hora), evento in eventos_ordenados:
    print(f"Día {dia} a las {hora}: {evento}")