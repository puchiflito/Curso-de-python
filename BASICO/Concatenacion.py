#Formas de concatenar

texto1 = "Hola"
texto2 = "Mundo"
texto = texto1 + " " + texto2
print(texto)

saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
print(saludoFinal)

print(f"Saludo: {texto1}, {texto2}")