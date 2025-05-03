cantidad_positivos=0
cantidad_negativos=0
par=0
impar=0
for i in range (6):
    num= int(input("Ingrese 10 números: "))
    
    if num >= 0:
        cantidad_positivos +=1
    elif num < 0:
        cantidad_negativos +=1
    if num % 2 == 0:
        par+=1
    elif num % 2 != 0:
        impar +=1
    
        
                
    
print(f"""Cantidad de números positivos {cantidad_positivos}
cantidad números negativos {cantidad_negativos}
cantidad números pares {par}
cantidad números impares {impar}""") 
   