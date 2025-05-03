num1=0
num2= int(input("Ingrese el segundo número: "))

inicio=num1
fin=num2+1

suma_total=0
for numero in range(inicio,fin):
    suma_total += numero

print(f"La suma de los numeros enteros entre {num1} y {num2} es: {suma_total}")