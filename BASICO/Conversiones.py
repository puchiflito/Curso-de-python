"""Es donde se puede convertir de un tipo de dato a otro, ejemplo: de caracter a entero
y viceversa
int() puede tomar un literal float o string como argumento y devuelve un valor de tipo class 'int'.
float() puede tomar como argumento un literal de int o de cadena y devuelve un valor de la class 'float'.
str() puede tomar un literal de float o int como argumento y devuelve un valor de la class 'str'."""



numero1 = "35"
numero2 = "18"
print(numero1 + numero2) # aca se esta concatenando dos variables

# Se esta convirtiendo de caracter STR a numero entero INT
num1 = int(numero1)
num2 = int(numero2)
print(num1 + num2)

#Se esta convirtiendo de numero entero INT a caracter STR
caracter = str(num1)
caracter1 = str(num2)
print(caracter + caracter1) 