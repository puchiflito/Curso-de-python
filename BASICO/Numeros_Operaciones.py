"""Se va a mostrar los operadores matematicos, tipos de operadores"""

entero = 23 #Numero entero 
decimal = 31.78 #Numero decimal con coma
complejo = 12 + 5j
booleano = True #Verdadero o falso 

print(entero)
print(decimal)
print(complejo)
print(booleano)

num1 = 20
num2 = 4
print(f"La suma es:{num1} + {num2}") #Una forma de unir tanto numeros como caracter
print("Suma: ", num1 + num2)  #Otra forma de concatenar numeros y caracteres
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
print("Division: ", num1 / num2) #Con decimal
print("Division exacta: ", num1 // num2) #Numero entero
print("Potencia: ",(num1 ** num2))