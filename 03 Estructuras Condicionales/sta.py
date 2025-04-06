import random
numeros_aleatorios = [random.randint(1,100) for i in range (50) ]

from statistics import mode, median, mean 
lista = numeros_aleatorios
resultado_mean = mean(lista)#cacula la media
print("media: ",resultado_mean)
resultado_median = median (lista) #calcula la mediana
print ("mediana: ",resultado_median)
resultado_mode = mode (lista)#calcula la moda
print ("moda: ",resultado_mode)

if resultado_mean > resultado_median > resultado_mode:
    print ("Sesgo positivo o a la derecha")
elif resultado_mean < resultado_median < resultado_mode:
    print("Sesgo negativo o a la izquierda")
elif resultado_mean == resultado_median == resultado_mode:
    print("Sin sesgo")