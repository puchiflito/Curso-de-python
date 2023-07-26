#Break: permite salir de un bucle cuando se cumple una condicion

"""for numero in range(1, 6):
    if numero == 3:
        break
    print("El numero es: {0}".format(numero))

print("Bucle terminado")"""

#Continue: Omite una parte del bucle cuando se cumple una condicion y continua el resto

"""for numero in range(1, 6):
    if numero == 3:
        continue
    print("El numero es: {0}".format(numero))

print("Bucle terminado")"""

#Pass: permite continuar con una sentencia o funcion que ya no tiene o aun no tiene un bloque de codigo
# sirve para cuando alguna funcion o bucle no tenga una instruccion y no de error
for numero in range(1, 6):
    if numero == 3:
        pass
    print("El numero es: {0}".format(numero))

print("Bucle terminado")