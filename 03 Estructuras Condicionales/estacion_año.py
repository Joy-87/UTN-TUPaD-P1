def determinar_estacion(hemisferio, mes, dia):
    
    hemisferio = hemisferio.upper()
    if hemisferio == 'N':
        if mes == 12 and dia >= 21:
            return "Invierno"
        elif mes == 1 or mes == 2:
            return "Invierno"
        elif mes == 3 and dia <= 20:
            return "Invierno"
        elif mes == 3 and dia >= 21:
            return "Primavera"
        elif mes == 4 or mes == 5:
            return "Primavera"
        elif mes == 6 and dia <= 20:
            return "Primavera"
        elif mes == 6 and dia >= 21:
            return "Verano"
        elif mes == 7 or mes == 8:
            return "Verano"
        elif mes == 9 and dia <= 20:
            return "Verano"
        elif mes == 9 and dia >= 21:
            return "Otoño"
        elif mes == 10 or mes == 11:
            return "Otoño"
        elif mes == 12 and dia <= 20:
            return "Otoño"
        else:
            return "Fecha inválida"
    elif hemisferio == 'S':
        if mes == 12 and dia >= 21:
            return "Verano"
        elif mes == 1 or mes == 2:
            return "Verano"
        elif mes == 3 and dia <= 20:
            return "Verano"
        elif mes == 3 and dia >= 21:
            return "Otoño"
        elif mes == 4 or mes == 5:
            return "Otoño"
        elif mes == 6 and dia <= 20:
            return "Otoño"
        elif mes == 6 and dia >= 21:
            return "Invierno"
        elif mes == 7 or mes == 8:
            return "Invierno"
        elif mes == 9 and dia <= 20:
            return "Invierno"
        elif mes == 9 and dia >= 21:
            return "Primavera"
        elif mes == 10 or mes == 11:
            return "Primavera"
        elif mes == 12 and dia <= 20:
            return "Primavera"
        else:
            return "Fecha inválida"
    else:
        return "Hemisferio inválido. Por favor, ingrese 'N' o 'S'."
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ")
try:
    mes = int(input("Ingrese el número del mes (1-12): "))
    dia = int(input("Ingrese el día del mes (1-31): "))
except ValueError:
    print("Entrada inválida para mes o día. Por favor, ingrese números.")
    exit()

# Determinar e imprimir la estación
estacion = determinar_estacion(hemisferio, mes, dia)       
print(f"En el hemisferio {hemisferio.upper()} el {dia} de {mes} es {estacion}.")       
        
