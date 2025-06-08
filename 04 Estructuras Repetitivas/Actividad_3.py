num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))

if num1 < num2:
    inicio=num1+1
    fin= num2
else:
    inicio= num2+1
    fin=num1

suma_total=0
for numero in range(inicio,fin):
    suma_total += numero

print(f"La suma de los numeros enteros entre {min(num1,num2)} y {max(num1,num2)} (excluyendolos) es: {suma_total}")