"""class Cuenta():

    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

        # Metodo GET

    def get_Saldo(self):
        return self._saldo
        
    def get_Propietario(self):
        return self._propietario

    def get_Moneda(self):
        return self._moneda
        
        # Metodo SET
    def set_Moneda(self, moneda):
        self._moneda = moneda




cuenta1 = Cuenta("Oscar Garcia", 15000, "Soles")
print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())
cuenta1.set_Moneda("Dolares")
print(cuenta1.set_Moneda())



sirve leer o modificar propiedades dentro de una clase, es mas para los atributos
de las clases que estan encapsuladas, que no se pueden ver desde afuera
"""
class Cuenta():
    def __init__(self, pro, sal, mon):
        self._propietario = pro
        self._saldo = sal
        self._moneda = mon
        
    def get_Saldo(self):
      return self._saldo

    def get_Propietario(self):
      return self._propletario
    
    def get_Moneda(self):
      return self._moneda

    #Metodo Set

    def set_Moneda(self, moneda):
      self._moneda = moneda

cuenta1 = Cuenta("scar Garcia", 15888, "Soles")
print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())
cuenta1.set_Moneda("Dolares")
print(cuenta1.get_Moneda())
