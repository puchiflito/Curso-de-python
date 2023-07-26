"""AND es el Y
OR es si o no
NOT es el no"""


distancia = 1200
numeroHermano = 3
salarioPadres = 1500

tieneBeneficio = False

#El operador AND obliga a que las dos condiciones sean verdaderas.... En cambio el OR es una de las dos es verdadera
if (distancia > 1000 and numeroHermano > 2) or salarioPadres < 2000:
    tieneBeneficio = True