"""Es una evaluacion de una condicion para la asignacion de un valor en una variable

string sexo:
sexo = (10 > 2) ? "masculino" : "femenino";

"""
#Asi se puede simular un operador ternario en Python no existe ese operador
sexo = ("Hombre", "Mujer")

posicion = True
sexo = sexo[posicion] #Mujer
print(sexo)
sexo = sexo[not posicion] #hombre
print(sexo)
