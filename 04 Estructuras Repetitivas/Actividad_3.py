print("""suma de todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. """)
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
num_1 = num1+1
while num_1 < num2:
   
    suma = num_1+ suma 
    num_1 = num_1 +1
    print(suma)