"""Son similares a las lista, solo que se guardan con clave valor
clave = seria el indice
valor = elemento"""

diccionario = {
    'IDE':'Intergrade Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)
#Largo del diccionario
print(len(diccionario))
# Acceder a un elemento
print(diccionario['IDE'])
# Otra forma de recuperar elemento 
print(diccionario.get('OOP'))
# Modificar elemento
diccionario['IDE'] = 'intergrade development environment'
print(diccionario)
# Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)
# Solo las llaves
for termino in diccionario.keys():
    print(termino)
# Solo los valores
for valor in diccionario.values():
    print(valor)

# Comprobar si existe en el diccionario, se debe respetar el valor de la llave
print('IDE' in diccionario)
# Agregar un elemento, no es posible agregar llaves duplicadas, si agregamos una llave existente,
# sobreescribe la llave con nuevo valor
diccionario['PK'] = 'Primary Key'
print(diccionario)
#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)
#Limpiar un diccionario
diccionario.clear()
print(diccionario)
#Eliminar diccionario
del diccionario
print(diccionario)