num=int(input("ingrese un número entero: "))
digitos=len(str(num))
while True:
    if num>=0:
        print (f"El número ingresado tiene {digitos} digitos")
    else:
        print (f"El número ingresado tiene {digitos} digitos, incluyendo el signo")
    break