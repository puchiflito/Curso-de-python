"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""
# UNA FORMA DE HACERLO

def max(n1, n2):
    if n1 > n2:
        print(f"{n1} es mayo que {n2}")
    else:
        print(f"{n2} es mayor que {n1}")

max(5, 6)


