"""
Paquetes:
Directorios (carpetas) donde se almacenan modulos relacionados entre si.

¿Para que sirve?
Para organizar mejor el codigo y poder reutilizarlos mejor

¿Como se crea un paquete?
crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace __init__.py es convertir un directorio en un modulo (paquete)
que contiene otros modulos, y esto lo hace para poder importarlos

"""


import funcionesNumericas 
import funcionesCadena

print(funcionesNumericas.mutiplicar(5, 6))

print(funcionesCadena.contarLetras("Hola la otra forma de import no sale"))

