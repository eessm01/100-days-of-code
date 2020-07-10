# Otra forma de leer archivos CSV con cabeceras, es utilizar el 
# objeto DictReader en vez de reader, y así acceder solo al 
# valor de las columnas deseadas, por su nombre:

from csv import DictReader

with open('datos_meteorologicos.csv', 'r') as archivo:
    documento = DictReader(archivo, delimiter=';', quotechar='"')
    for fila in documento: 
        print(fila['ID'])
