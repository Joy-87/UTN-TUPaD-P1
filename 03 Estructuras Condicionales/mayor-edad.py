while True: #le pide al usuario la edad en caso de que ingrese un dato incorrecto
    try: #try-except para capturar el valueerror y que no se bloquee el programa 
        edad = int(input("Ingrese su edad: ") )
        if edad >= 18:    
            print("Sos mayor de edad")
        else:
            print("Sos menor de edad")
        break    
    except ValueError:
        print("Valor incorrecto. Ingrese otro ") 

             