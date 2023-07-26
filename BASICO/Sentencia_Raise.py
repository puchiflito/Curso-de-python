# Sirve para lanzar de forma intencional exepciones en python

def evaluarNota(nota):
    if nota < 0:
        raise ValueError("Valor incorrecto")
    elif nota >= 16:
        print("Exelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")

evaluarNota(13)