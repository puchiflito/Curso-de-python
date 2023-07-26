"""Son estructura de datos que nos permiten almacenar informacion
de distintos valores, serian como loa arreglos o arrays
Son estructura dinamica, que pueden mutar de tamaño"""

lista1 =["Oscar", 25, 98.3, True, "Flavio", 56.3]
print(lista1)
print(lista1[2]) #Solo para ver que valor hay en esa posicion
print(lista1[-1]) # Nos muestra el ultimo valor de la lista

#Operaciones basica de las listas
print(lista1[0:3]) #Nos muestra de la posicion inicial 0 a la posicion 2, siempre es un menos del ultimo numero

lista1.append("UskokruM2010") #Una forma de agregar un elemento a loa lista
print(lista1)

lista1.insert(4, "Peru") #Se agrega un elemento en esa posicion
print(lista1)

lista1.extend(["Alejandro", 110, False]) #Se puede agregar una lista dentro de otra lista
print(lista1)

print(lista1.index("Flavio")) #Nos muestra en que indice esta 

lista1.remove(56.3) #Es para eliminar un elemento de la lista
print(lista1)

lista1.pop() #Elimina el ultimo elemento de la lista
print(lista1)

lista2 = ["Chiclayo", "Irma"]
lista3 = lista1 + lista2 # Se concatenan las listas
print(lista3)

print("UskokruM2010" in lista1) #Nos arroja un valor booleano, true si esta y false si no esta


nombres = ['juan', 'karla', 'ricardo', 'maria']
print(nombres[-1]) #de manera inversa, osea de atras pa adelante
nombres[3] = 'Ivone' #Cambia el valor del indice de la lista
print(nombres)
#Iterar en una lista
for nombre in nombres:
    print(nombre)
else:
    print("no hay mas nombre en la lista")

# Preguntar cuan largo es la lista
print(len(nombres))

