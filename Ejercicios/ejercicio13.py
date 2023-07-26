"""
Definir una funcion inversa() que calcule la inversion de una cadena. Por ejemplo
la cadena 'estoy probando', deberia devolver la cadena 'odnaborp yotse'"""

def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

print(invertir_cadena_manual("Hola de nuevo"))