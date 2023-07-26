class Curso():
    """nombre = "Matematicas"
    creditos = 5
    profesion = "Ingenieria Civil"
    """

#Estado inicla de la clase
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial" # Propiedad encapsulamiento

    def mostrarDatos(self):
        dat = "Nombre: {0} / Credito: {1} / Modo de imparticion{2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado")
        else:
            print("No es necesario asignar un docente...")

    def __verificarDocente(self):
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
    
    def __str__(self):
        texto = "Nombre: {0} - Creditos: {1}"
        return texto.format(self.nombre, self.creditos)
    

curso1 = Curso("Matematicas", 5, "Ingenieria Civil")
print(curso1)
curso1.mostrarDatos()


"""curso2 = Curso("Lenguaje", 4, "Ingenieria")
print(curso2.nombre)"""

# Para encapsular se debe colocar doble guion bajo delante de la variable a encapsular

# Para encapsular una funcion es igual agregando doble guion bajo adelante

"""
Para poder ver una variable encapsulada (oculto) debe estar 
dentro de la clase, como es en este ejemplo
"""