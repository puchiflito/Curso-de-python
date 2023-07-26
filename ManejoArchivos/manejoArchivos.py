"""file = open('ManejoArchivos\data1.txt', 'r') # La r corresponde a modo lectura
#print(file)
lineas = file.readlines()
print(lineas)
file.close()

# Cierra automaticamente despues de ejcutar las lineas
with open('ManejoArchivos\data2.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print(lineas)

print(lineas)
for l in lineas:
    print(l.replace('\n', '')) # cambiando el salto de linea por espacios vacios
  

with open('ManejoArchivos\data2.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n') # eliminando saltos de lineas
    print(lineas)


with open('ManejoArchivos\data2.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    pos = archivo.tell()
    print(pos) # posiscion del archivo
    print("El archivo tiene {0} caracteres de longitud".format(pos))


with open ('ManejoArchivos\data2.txt', 'r') as archivo:
    archivo.seek(7)
    pos = archivo.tell()
    print(pos)
    contenido = archivo.read()
    lineas = contenido,split('\n')
    print(lineas)

cuantos caracteres podemos leer

with open ('ManejoArchivos\data2.txt', 'r') as archivo:
    siguientes4 = archivo.read(4)
    print(siguientes4)

Muestra que tipo de archivo es. La r es de caracteres

with open ('ManejoArchivos\data2.txt', 'r') as archivo:
    print(type(archivo.read()))
Mientras que rb elo lee en bytes
with open ('ManejoArchivos\data2.txt', 'rb') as archivo:
    print(type(archivo.read()))
"""


with open('ManejoArchivos\data3.txt', 'w') as archivo:
    archivo.write('Oscar\nAlejandro\nFlavio23')