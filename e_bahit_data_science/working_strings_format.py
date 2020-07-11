"""CIENCIA DE DATOS CON PYTHON by Eugenia Bahit. 2 edition. pages 6-8"""

# copia de la cadena con la primera letra en mayusculas
cadena = 'bienvenido a mi aplicacion'
print(cadena.capitalize())

# minúsculas
print(cadena.lower())

# mayúsculas
print(cadena.upper())

# copia de la cadena convertiendo mayúsculas en munúsculas y vesceversa
print('Hola Mundo'.swapcase())

# copia de la cadena convertida den titulo
print('hola mundo lindo'.title())

# centrar un texto
cadena = 'bienvenido a mi aplicacion'.capitalize()
print(cadena.center(50, '*'))
print(cadena.center(50, ' '))

# alinear texto a la izquierda
print(cadena.ljust(50, '='))

# alinear texto a la derecha
print(cadena.rjust(50, '='))

# rellenando un texto anteponiendo ceros
numero_factura = 1575
print(str(numero_factura).zfill(12))