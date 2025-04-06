nombre = input("Ingrese su nombre ")
def opcion1():
    mayusculas = nombre.upper()
    print (mayusculas)

def opcion2():
    minusculas = nombre.lower()
    print(minusculas)

def opcion3():
    formato_titulo = nombre.capitalize()
    print (formato_titulo)
    
while True:
    try:
        opcion = int(input("Ingrese la opción deseada (1: Mayúsculas, 2: Minúsculas, 3: Capitalizar): "))
        if opcion in [1, 2, 3]:
            break  # Salir del bucle si la opción es válida
        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

if opcion == 1:
    opcion1()
elif opcion == 2:
    opcion2()
elif opcion == 3:
    opcion3()