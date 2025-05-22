def informacion_personal(nombre, apellido, edad, residencia):
   
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre_p = input("Ingresa tu nombre: ")
apellido_p = input("Ingresa tu apellido: ")
edad_p = int(input("Ingresa tu edad: ")) 
residencia_p = input("Ingresa tu residencia: ")

informacion_personal(nombre_p, apellido_p, edad_p, residencia_p)
