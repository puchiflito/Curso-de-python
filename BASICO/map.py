# Map: aplica una funcion a cada elemento de una lista iterable, devolviendo otra lista

def elevarCuadrado(num):
    # return num * num
    return pow(num, 2)

numeros = list(range(1,11))
print(numeros)

numerosElevados = list(map(elevarCuadrado, numeros))
print(numerosElevados)