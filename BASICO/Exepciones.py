#Es un error en tiempo de ejecucion (durante la ejecucion del programa)

numero1 = 20
numero2 = 0

#print("La division de {0} entre {1} es: {2}".format(numero1,numero2,(numero1/numero2)))

try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("No se puede dividir por 0")