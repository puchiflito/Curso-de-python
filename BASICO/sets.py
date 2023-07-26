# Sets: son colecciones desordenadas de objetos unicos
# No tiene indice

canasta = {'manzana', 'platano', 'pera', 'manzana', 'naranja', 'pera'}
print(canasta)

numeros = {1,3,5,8,3,4,12,1}
print(numeros)

a = set("abracadabra")
print(a)

planeta = {'Marte', 'Jupiter', 'Venus'}
print(planeta)

# Largo 
print(len(planeta))

# Revisar si esta presente un valor en el set, se puede hacer en todo las colecciones

print('Martes' in planeta)

# Agregar 
planeta.add('Tierra')
print(planeta)

# No soporta un elemento duplicado
planeta.add('Tierra')
print(planeta)

#Eliminar elemento, puede dar error si no se encuentra dentro del set
planeta.remove('Tierra')
# Elimina un elemento sin arrojar error
planeta.discard('Jupiters')

# Limpiar el set
planeta.clear()
print(planeta)

# Eliminar set
del planeta
print(planeta)