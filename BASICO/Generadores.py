"""Generadores: permite extraer valores de una funcion y almacenarlos 
de uno en uno en objetos iterables (que se pueden recorrer),
sin la necesidad de almacenar todo en la memoria RAM
"""

"""def generaMultiplos7(limite):
    numero = 1
    listanumeros = []

    while numero <= limite:
        listanumeros.append(numero * 7)
        numero = numero + 1
        
    return listanumeros #Retorna toda la lista creada

print(generaMultiplos7(10))"""


def generaMultiplos7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7 #Ceder, la instruccion yield genera un objeto iterable
        numero = numero + 1


obtieneMultiplos7 = generaMultiplos7(10)
print(obtieneMultiplos7)

"""for n in obtieneMultiplos7:
    print(n)
"""
# next() : retorna el siguiente elemento de un objeto iterable

print(next(obtieneMultiplos7))