muy_leve = 3
leve = 4
moderado = 5
fuerte = 6
muy_fuerte = 7

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print ("Muy leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve ( ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte( puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar daños a gran escala)")