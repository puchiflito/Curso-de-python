"""es una sentencia booleana osea se ejecuta una condicion"""

print("--Cursos--")
print("Matematicas - biologia - lengua - ciencias")

curso = input("ingrese el curso deseado: ")

if curso in ("Matematicas", "Biologia", "Lengua", "Ciencias"):
    print("Curso {0} seleccionado.".format(curso))
else:
    print("No existe ese curso")

condicion = True

if condicion:
    print('Condicion verdadera')
else:
    print('Condicion falsa')