"""Obtiene la raíz cuadrada de un número

A través del método de enumeración exahustiva, este programa
busca la raiz cuadrada de un número. 
Este tipo de algoritmo busca dentro de todas las posibles
soluciones.
"""

objetivo = int(input('Elige un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta} ')
else: 
    print(f'{objetivo} no tiene una raiz cuadrada exacta')