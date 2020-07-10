from csv import DictWriter


matriz = [
    dict(jugador='Juan', puntos=373, anio=1970),
    dict(jugador='Ana', puntos=124, anio=1983),
    dict(jugador='Pedro', puntos=901, anio=1650),
    dict(jugador='Rosa', puntos=300, anio=2000),
    dict(jugador='Juana', puntos=75, anio=1975),
]

cabeceras = ['jugador', 'puntos', 'anio']

with open('datos_con_cabecera.csv','w') as archivo:
    documento = DictWriter(archivo, delimiter='|', quotechar='"',
        fieldnames=cabeceras)
    documento.writeheader()
    documento.writerows(matriz)