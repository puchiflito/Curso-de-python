# Sintaxis de range (inicio <opcional>, fin <requerido>, incremento <opcianal>)
#Ejercicio 1. Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
for i in range(11):
    if i % 3 == 0:
        print(i)
#Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimir
for i in range(1,6):
    i = i + 1
    print(i)
#Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
for i in range(2, 10):
    i = i + 2
    print(i)