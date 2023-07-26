"""
Son funciones anonimas que sirven para abreviar o resumir una funcion normal,
para convertirla en una expresion mas simple.
"""

"""def sumar(n1, n2):
    return n1 + n2

print(sumar(12, 15))"""

#Toda funcino lambda se puede convertir a una funcion normal, no viceversa

sumar = lambda n1, n2: n1 + n2

print(sumar(45,14))