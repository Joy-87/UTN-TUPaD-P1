
def decimal_binario_opcion1(num_decimal):
    # Validamos que sea un entero y no sea negativo
    if not isinstance(num_decimal, int):
        print("Error: Por favor, ingrese un NÚMERO ENTERO.")
        return None # Devolvemos None para indicar que hubo un error

    if num_decimal < 0:
        print("Error: El número debe ser positivo o cero.")
        return None # Devolvemos None para indicar que hubo un error
    
    # Resto de la lógica de la función 
    if num_decimal == 0:
        return "0"
    
    cociente = num_decimal // 2
    resto = num_decimal % 2
    
    if cociente == 0:
        return str(resto)
    else:
        
        return decimal_binario_opcion1(cociente) + str(resto)


print(f"10 en binario: {decimal_binario_opcion1(10)}") 