"""Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas,
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir
5
4
3
2
1
y asi de cualquier numero factorial.
Si es numeros negativos no debe mostrar nada"""

def imprimirNumeroRecursiva(numero):
    if numero >=1:
        print(numero)
        imprimirNumeroRecursiva(numero - 1)
    elif numero == 0:
        return 
    elif numero < 0:
        print("Valor incorrecto...")
    


imprimirNumeroRecursiva(5)