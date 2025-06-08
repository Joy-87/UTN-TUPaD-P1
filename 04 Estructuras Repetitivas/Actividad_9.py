cantidad=0
suma=0
for i in range (100):
    num= int(input("Ingrese 100 números: "))
    suma += num
    cantidad=i+1
print(f"La suma total de los {cantidad} números ingresados es: {suma} ")
media=float (suma) / (cantidad)
print (f"La media de los valores ingresados es: {media}")