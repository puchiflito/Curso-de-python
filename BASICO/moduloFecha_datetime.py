"""import datetime

fechaActual = datetime.datetime.now()
print(fechaActual)"""

"""from datetime import datetime

fechaActual =datetime.now()
print(fechaActual)

# Crear fecha perzonalizada

fecha = datetime(2020,11,5) # Años Mes Dia
print(fecha)"""

import datetime

"""fechaActual = datetime.datetime.now()
fechaActual2 = datetime.datetime.strftime(fechaActual, "%d/%m/%Y %H:%M:%S")
print(fechaActual2)
"""
fechaActual = datetime.datetime.now()
#fechaActual3 = datetime.datetime.strftime(fechaActual, "%b %d %Y %H:%M:%S")
#print(fechaActual3)


# Cambia de caracter a formato fecha
fechaTexto = 'Dec 06 2020 12:56:11'
fechaActual4 = datetime.datetime.strptime(fechaTexto, '%b %d %Y %H:%M:%S')
print(fechaActual4)

# Muestra que numero de dia es
dia = datetime.datetime.strftime(fechaActual, '%d')
print(dia)

# Para ver la hora actual
horaActual = datetime.datetime.strftime(fechaActual, '%H:%M:%S')
print(horaActual)


# Restar dias 
fechaPasada = datetime.datetime(2020,10,23)
diferencia = fechaActual - fechaPasada
print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds())


dia_delta = datetime.timedelta(days=5)
fechaInicial = datetime.date.today()
print(fechaInicial)
fechaFutura = fechaInicial + dia_delta
print(fechaFutura)