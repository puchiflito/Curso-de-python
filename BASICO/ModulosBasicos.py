"""ALGUNAS LIBRERIAS ESTANDAR
MODULO OS
import os: es para interactuar con el sistema operativo
print(os.getcwd()) devuelve el directorio de trabajo actual
print(dir(os)) devuelve una lista con las funciones del modulo
print(help(os)) devuelve documentacion del modulo

MODULO SHUTIL
import shutil tareas diarias de administracion de archivos y directorios. Copiar ficheros mover
shutil.move("C:\Videos\Video1.txt", "C: \\Video1.txt")

MODULO GLOB
import glob listas de archivos a partir de busquedas con comodines en directorios
print(glob.glob('.py'))

MODULO RE
import re para tabajar con expresiones regulares
print(re.findall(r'\bf[a-z]*', 'tres felices tigres comen trigo')) muestra palabras que comienzan con f

MODULO MATH
import math modulo matematico
print(math.pi) el valor de pi

MODULO RANDOM
import random para realizar selecciones a la azar
print(random.radiant(0,10000)) rango del radian de 0 a 10000
print(random.random()) numero a la azar
print(random.randomrange(7)) ranfo qntre 0 y 7

MODULO STATISTICS
import statistics calcula propiedades de estatida basica(la media, madiana, varianza, etc) de datos numericos
datos = [2.75,1.75,1.25,0.25,0.5,1.25,3.5]
print(statistics.mean(datos))
print(statistics.median(datos))
print(statistics.variance(datos))

#MODULO URLLIB.REQUEST
import urllib.request #modulo para acceder a internet y procesar sus protocolos
with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    print(html)

DEVUELVE LA PAGINA EN FORMATO HTML

MODULO DATE DATETIME
from datetime import date trabajar con fechas
hoy = date.today()
print(hoy) imprime la fecha de hoy

MODULO LOGGING
import logging
logging.debug('informacion de depuracion')
logging.info('Mensaje informativo')
logging.warning('Atencion: archivo de configuracion %s no se encuentra','server.conf')
logging.error('Ocurrio un error')
logging.critical('Error critico -- cerrando')
"""


