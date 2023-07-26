"""Es una forma de comprobar si una restpuesta o valor es verdadero o falso
dependiendo de la evaluacion de la condicion se mostrara un resultado verdad o falso-"""

edad = int(input("Ingrese su edad: ")) #solo ingresa valores numericos enteros por INT

if edad > 18: #verdadero
    print("Eres mayor de edad")
elif edad == 18: #Otra opcion de verdadero
    print("Tienes 18 años no eres mayor de edad todavia")
else: #falso
    print("No eres mayor de edad")

