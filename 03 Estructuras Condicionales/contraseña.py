contrasenia = input("Ingrese una contraseña que tenga entre 8 y 14 caracteres: ")
longitud_contrasenia = len(contrasenia)

if 8 <= longitud_contrasenia <= 14:
    print("La contraseña tiene una longitud válida.")
else:
    print("La contraseña debe tener entre 8 y 14 caracteres.")