"""Ciencia de Datos con Pyton. Pag. 31
"""

from csv import writer


matriz = [
    ['Juan', 373, 1970],
    ['Ana', 124, 1983],
    ['Pedro', 901, 1650],
    ['Rosa', 300, 2000],
    ['Juana', 75, 1975],
]

with open('datos.csv', 'w') as archivo:
    documento = writer(archivo, delimiter='|', quotechar='"')
    documento.writerows(matriz)

