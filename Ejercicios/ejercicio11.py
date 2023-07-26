"""
Convertidor de grados
realizar dos funciones para convertir de grados a fahrenheit, y viceverza
formula: 
C° a F°: se multiplica 1.8 y se suma 32
F° a C°: se resta 32 y se divide 1.8"""


def pasar_a_fahrenheit(c):
    pasaje = (c * 1.8) + 32
    print(f"la temperatura en fahrenheit es: {pasaje}")

def pasar_a_grados(f):
    pasar = (f - 32) / 1.8
    print(f"La temperatura en celsius es: {pasar}")

pasar_a_fahrenheit(32)
pasar_a_grados(100)