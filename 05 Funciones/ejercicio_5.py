def segundos_a_horas(segundos):
   
    return segundos / 3600 # 1 hora = 3600 segundos

try:
    segundos_usuario = int(input("Ingresa una cantidad de segundos: "))
    horas = segundos_a_horas(segundos_usuario)
    print(f"{segundos_usuario} segundos equivalen a {horas:.2f} horas.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero para los segundos.")
