class Persona():

    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom
    
    def mostrarNombresCompletos(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def datos(self):
        print(self.mostrarNombresCompletos())

class Estudiante(Persona):

    def __init__(self, apePat, apeMat, nom, pro):
        super().__init__(apePat, apeMat, nom) #Sirve para heredar el iniciador de la clase padre
        self.profesion = pro

    def datos(self):
        super().datos() #Herencia
        print("Profesion: {0}".format(self.profesion))


estu1 = Estudiante("Torres", "Lopaz", "Juan", "Ingenieria Civil")
#print(estu1.mostrarNombresCompletos())
#print(estu1.profesion)
estu1.datos()