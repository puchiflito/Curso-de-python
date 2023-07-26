"""
Calculadora de Impuestos:
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

def calcular_impuesto(pago_sin_impuesto, impuesto):
    print(f"Pago sin impuesto es: {pago_sin_impuesto}")
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    print(f"El pago con impuesto es: {pago_total}")


calcular_impuesto(5000, 0.21)
