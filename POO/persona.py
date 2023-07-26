"""
¿En que consiste la programacion orientada a objetos?
En trasladar la naturaleza de los objetos de la vida real a codigo
de programacion (en algun lenguaje de programacion como python).

Los objetos de la realidad tienen caracteristicas (atributos o propiedades)
y funcionalidades o comporatamientos (funciones o metodos).

Ventajas:
Modularizacion (division en pequeñas partes) de un programa completo.
Codigo fuente muy reutilizable.
Codigo fuente mas facil de incrementar en el futuro y mantener.
Si existe un fallo en una epqueña parte del codigo el programa completo no debe fallar 
necesariamente. Ademas, es mas facil de corregir esos fallos.
Encapsulamiento: Ocultamiento del funcionamiento interno de un objeto.
"""


class Persona():
    #Asignando atributos
    apellido = ""
    nombre = ""
    edad = 0
    despierto = False

    #Asignando funciones a la clase
    def despertar(self):
        #self: parametro que hace referencia a la instancia perteneciente a la clase
        self.despierto = True
        print("Buen dia.")

persona1 = Persona()
persona1.apellido = "Garcia Fuentes" #Asignando y accediendo a la variable
print(persona1.apellido)
persona1.despertar() #Llamando a la funcion de la clase
print(persona1.despierto)

persona2 = Persona()
persona2.apellido = "Paz Torres"
print(persona2.apellido)
print(persona2.despierto)