"""Las funciones son un conjunto de instrucciones que nos ayudan a no repetir lineas de codigo
y se pueden reutilizar

def evaluarSueldoMinimo(sueldo): 
    if sueldo >= 850:
        print("Cobras el sueldo minimo")
    else:
        print("No cumples con el sueldo minimo")


evaluarSueldoMinimo(1000)

def mi_funcion(nombre, apellido):
    print("Saludos")
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion('Juan', 'Perez')

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
# print(f"Resultado sumar: {sumar(5, 3)}")
print(resultado)
ARGUMENTOS VARIABLES EN FUNCIONES
#Con * delante de la variable se transforma como una tupla, que se puede pasar varias parametros
def listarNombres(*nombres): 
    for nombre in nombres:
        print(nombre)

listarNombres("juan", "karla", "maria", "ernesto")
ARGUMENTOS VARIABLES LLAVE-VALOR
se recibe un diccionario

def listarTermino(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')
listarTermino(IDE = 'integrated developement eviroment', PK = 'primary key')

DISTINTOS TIPOS DE DATOS COMO ARGUMENTOS
solo se puede iterar en tipos de datos string, no numericos"""

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ["Juan", "Karla", "Guillermo"]
desplegarNombres(nombres)
desplegarNombres("Carlos")# Deletrea la palabra
desplegarNombres((10,11)) # aca si itera ya que esta dentro de una tupla
