"""Obtiene la raiz cuadrada de un número

Este programa usa el algoritmos de búsqueda binaria
para obtener el resultado.
"""

objetivo = int(input('Ingrese un número: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)  #regresa el mayor de esos dos valores
respuesta = (bajo + alto) / 2
iteraciones = 0

while abs(objetivo - respuesta**2) >= epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (bajo + alto) / 2
    iteraciones += 1

print(f'En {iteraciones} iteraciones y epsilon = {epsilon}, se encontró la raiz cuadrada de {objetivo} que es {respuesta}')



