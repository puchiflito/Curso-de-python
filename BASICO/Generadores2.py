"""Cuando indicamos un * adelante del parametro de una funciona, estamos indicando que
se va a recibir un numero indeterminado de parametros. Ademas esos parametros se recibiran
en forma de tuplas"""

def devuelveLenguajes(*lenguaje):
    for leng in lenguaje:
        yield from leng

lenguajeObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Javascript")

print(next(lenguajeObtenidos))
print(next(lenguajeObtenidos))