def calcular_imc(peso, altura):
    
    if altura <= 0:
        return None # Evitar división por cero o altura inválida
    return peso / (altura ** 2)


try:
    peso_usuario = float(input("Ingresa tu peso en kilogramos (ej. 70.5): "))
    altura_usuario = float(input("Ingresa tu altura en metros (ej. 1.75): "))

    imc = calcular_imc(peso_usuario, altura_usuario)

    if imc is not None:
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    else:
        print("No se puede calcular el IMC con la altura proporcionada (debe ser mayor que cero).")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos para peso y altura.")
