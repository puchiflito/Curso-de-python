"""Una TUPLA es una estructura de Python que permite almacenar distintos valores
, y no se pueden modificar"""

tupla = (1, 2, 3)
print(tupla)

tupla2 = (7, "Oscar", True, 450.1, 16 + 7j, 15, "Felicidad", False)
print(tupla2)

tupla3 = (9, 3, (4, 5, 6)) #Puede haber una tupla dentro de otra
print(tupla3)

print(tupla2[1]) #Es para acceder o mostrar el valor dentro de una tupla
print(tupla2[-1]) #Nos muestra el ultimo valor de la tupla
print(tupla2[0:4]) #Imprime los valores dentro de ese rango especificado, pero un rango menos a mostrar

a,b,c = tupla #Se asigna los valores por separados
print(a)
print(b)
print(c)

#Concatenar TUPLAS
tuplaFinal = tupla + tupla3
print(tuplaFinal)

#Contar cuantas veces se repite un valor
print(tuplaFinal.count(3))

frutas = ("Naranja","Platano","Guayaba")
#Recorrer una tupla
for fruta in frutas:
    print(fruta, end=" ") #se imprime en una linea con espacios

#cambiar valor de una tupla
frutasLista = list(frutas) #esto cambia a una lista
frutasLista [0] = "Pera"
frutas = tuple(frutasLista) #convierte a tupla

print("\n",frutas)

#Eliminar la tupla completa
#del frutas
