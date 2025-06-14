
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#    Permití al usuario:
#    • Consultar el stock de un producto ingresado.
#    • Agregar unidades al stock si el producto ya existe.
#    • Agregar un nuevo producto si no existe.

stock_productos = {
    "Leche": 50,
    "Pan": 100,
    "Huevos": 30,
    "Azúcar": 25
}

print("--- Gestión de Stock de Productos ---")

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades / Nuevo producto")
    print("3. Mostrar todo el stock")
    print("4. Salir")

    opcion = input("Ingrese su opción (1-4): ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ").capitalize()
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no se encuentra en el stock.")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto a agregar/actualizar: ").capitalize()
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de unidades a agregar para '{producto}': "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa. Intente de nuevo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        if producto in stock_productos:
            stock_productos[producto] += cantidad
            print(f"Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}.")
        else:
            stock_productos[producto] = cantidad
            print(f"Se agregó el nuevo producto '{producto}' con un stock inicial de {cantidad} unidades.")
    
    elif opcion == '3':
        print("\n--- Stock Actual ---")
        if stock_productos:
            for producto, stock in stock_productos.items():
                print(f"{producto}: {stock} unidades")
        else:
            print("El stock está vacío.")

    elif opcion == '4':
        print("Saliendo del programa de gestión de stock. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")