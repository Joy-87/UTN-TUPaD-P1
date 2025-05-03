num=str(input("Ingrese un número: "))
num_invertido=""
for i in range (len(num) -1,-1,-1):
    num_invertido+=num[i]
print(num_invertido)