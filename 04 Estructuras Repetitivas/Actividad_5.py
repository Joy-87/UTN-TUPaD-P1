import random
input("""Bienvenido!!
      Ingrese el número correcto y gané """)
intentos=0
i=random.randint (0,10)  

while True:  
    num=int(input ("Ingrese un número del 0 al 9: "))
    intentos += 1
    if i  == num :
        print ("Ganaste!!")
        print(f"Realizaste {intentos} intentos")
        break
    else:
        print ("segui partcipando")
       
