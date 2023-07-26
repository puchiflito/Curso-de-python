"""Crear una funcion para sumar los valores recibido de tipo numerico,
utilizando argumentos variables *args como parametros de la funcion
y regresar como resultado la suma de todos los valores pasados como argumentos"""

def sumar_valores(*args):
    resultado = 0
    #Recorre los valores de la variable args
    for valor in args:
        #Para ser mas sencillo seria: resultado = resultaod + valor
        resultado += valor
    return resultado

print(sumar_valores(3, 5, 9))