texto = "Bienvenido al canal"
print(texto)
print(texto.lower()) #lo hace todo en minuscula
print(texto.upper()) #lo hace en mayuscula
print(texto.title()) #coloca en mayuscula la primera letra de cada palabra
print(texto.find("al")) #nos muestra la ubicacion de la pablara
print(texto.count("a")) #nos cuenta cuantas veces se repite lo que buscamos

textoFinal = texto.replace("e", "3") #reemplaza lo viejo por lo nuevo
print(textoFinal)

valor = texto.isnumeric() #es para saber si nuestro texto tiene valor numerico
print(valor)

