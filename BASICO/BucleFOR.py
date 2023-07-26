"""Bucles: son estructura de control de flujo que repiten 1 o varias
lineas de codigo"""

for num in range(0,10):
    print("Valor actual: {0}".format(num))


for i in range(1,13):
    print("{0} * {1} es: {2}".format(i, i, (i * i)))



for nom in ["karen", "Oscar", "Hector", "Leonardo"]:
    print("Cantidad de letras de {0} es: {1}".format(nom,len(nom)))

"""range(): Crea una lista inmutable de numeros enteros en sucesion aritmetica"""

numeros = range(5) #[0,1,2,3,4] muestra un valor menos del numero asignado
print(numeros[2])

numeros1 = range(4,10) # [4,5,6,7,8,9]
print(numeros1[2])

numeros2 = range(10,100,8) #El primer numero es el comienzo, el segundo es el final y el tercero esel incrmento
print(numeros2[9])