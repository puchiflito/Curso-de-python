"""
Modulo:
Es un archivo con extension .py o .pyc (Pythoon compilado), que posee su propio espacio de 
nombres y que pueda contener variables, funciones, clases o incluso otros modulos.

¿Para que sirve?
Para organizar mejor el codigo y poder reutilizarlo mejor.
Modularizacion y reutilizacion.

Para importar archivos solamente deben de tener caracteres
"""

#Una forma de importar 

#import FuncionesMatematicas
#print(FuncionesMatematicas.suma(5, 6))

from modulos.FuncionesMatematicas import suma

print(suma(5,6))

