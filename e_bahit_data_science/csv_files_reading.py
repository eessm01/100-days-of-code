"""Ciencia de Datos con Pyton. Pag. 27-30

El formato CSV deriva su nombre del inglés «comma separated values»
(valores separados por coma), definido en las RFC 4180. Se trata de
archivos de texto plano, destinados al almacenamiento masivo de 
datos. Es uno de los formatos más simples para efectuar análisis 
de datos.

Un archivo CSV se encuentra formado por una cabecera que define 
nombres de columnas, y las filas siguientes, tienen los datos 
correspondientes a cada columna, separados por una coma. Sin 
embargo, muchos otros símbolos pueden utilizarse como separadores
de celdas. Entre ellos, el tabulado y el punto y coma son igual 
de frecuentes que la coma.

Python provee de un módulo propio llamado csv, que facilita el 
parseo de los datos de archivos CSV, tanto para lectura como 
escritura.
Este módulo, se utiliza en combinación con la estructura with 
y la función open, para leer o generar el archivo, y el módulo CSV 
para su análisis (parsing).
"""

from csv import reader

with open('datos_meteorologicos.csv', 'r') as archivo:
    documento = reader(archivo, delimiter=';', quotechar='"')
    # lee sin cabeceras
    cabeceras = next(documento)
    for fila in documento:
        print(fila)
        print('|'.join(fila))
        print(' '.join(fila))
        print(fila[1])




