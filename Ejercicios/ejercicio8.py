"""Crea una funcion para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la multiplicacion de todos los valores pasados
como argumentos"""

def multiplicacion(*args):
    r = 1
    for i in args:
        r *= i
    return r

print(multiplicacion(5, 5, 5, 5))