def saludar_usuario(nombre):
   
    return f"¡Hola {nombre}!"


nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)
