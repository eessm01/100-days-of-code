"""Ciencia de Datos con Pyton. Pag. 24-26

Cada vez que se “abre” un archivo se está creando un puntero 
en memoria.
Este puntero posicionará un cursor (o punto de acceso) en un 
lugar específico de la memoria (dicho de modo más simple, 
posicionará el cursor en un byte determinado del contenido del 
archivo).
"""

# Con la estructura with y la función open(), puede abrirse un archivo
# en cualquier modo y trabajar con él, sin necesidad de cerrarlo o 
# destruir el puntero, ya que de esto se encarga la estructura with.

# leyendo un archivo
with open('what-is-data-science.txt','r') as archivo:
    contenido = archivo.read()

print(contenido)



# escribiendo un archivo
contenido = """
    Este será el contenido del nuevo archivo.
    El archivo tendrá varias líneas.
"""

with open('writing-file.txt','w') as archivo:
    archivo.write(contenido)

