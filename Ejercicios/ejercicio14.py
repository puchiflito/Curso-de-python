global cuenta, opcion

def menu():
    print("1 Saldo")
    print("2 Extraccion")
    print("3 Deposito")

def mostrar_saldo():
    cuenta = 0
    print(f"Su saldo es: ${cuenta} pesos")



def extraccion():
    cuenta = 0
    extra = float(input("¿Cuanto dinero desea extraer?: "))
    r = extra - cuenta
    if cuenta == 0:
        print("No tiene saldo en su cuenta")
    else:
        print(f"Retiro ${r} pesos")
        print(f"Su saldo es de: {r}")
    
def depositar():
    cuenta = 0
    dep = float(input("¿Cuanto dinero desea depositar?: "))
    r = dep - cuenta
    print(f"Usted deposito ${r} pesos")
    print(f"Su saldo es de ${r} pesos")

menu()

opcion = int(input("Ingrese una opcion: "))


if opcion == 1:
    mostrar_saldo()
elif opcion == 2:
    extraccion()
elif opcion == 3:
    depositar()
else:
    if opcion >= 4:
        print("Opcion invalida intentelo de nuevo")


