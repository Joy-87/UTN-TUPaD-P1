suma=0
while True:
    num= int(input("Ingrese el número que decea sumar, si decea terminar oprima \"0\": ")) 
    
    if num > 0:
        suma = suma + num
        
    else:
        print(f"Usted ingreso \"0\". Fin de secuencia. El total es: {suma}")
        break
