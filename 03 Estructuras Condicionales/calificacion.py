while True:
    try:
        nota = float(input("Ingrese su nota: "))
        if nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")
        break
    except ValueError:
        print("Dato incorrecto.")  
    