"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(n1,n2,n3):
    while n1 > n2 and n1 > n3:
        print(f"{n1} es mayor de los tres")
        continue
    if n2 > n1 and n2 > n3:
        print(f"{n2} es mayor de los tres")
    else:
        print(f"{n3} es mayor que los anteriores")

max_de_tres(1, 0, 0)