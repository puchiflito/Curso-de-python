"""
Escribir una funcion sum() y una funcion multip() que sumen y multipliquen
respectivamente todos los numeros de una lista. Por ejemplo: sum([1,2,3,4]),
deberia dar 10 y multip([1,2,3,4]) deveria devolver 24"""
lista= [1, 2, 3, 4]

def sum(lista):
    r = 0
    for i in lista:
        r += i
        print(r)
def multip(lista):
    r = 1
    for i in lista:
        r *= i
        print(r)

sum(lista)
multip(lista)