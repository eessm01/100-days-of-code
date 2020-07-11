"""CIENCIA DE DATOS CON PYTHON by Eugenia Bahit. 2 edition. page 8"""

# contar cantidad de aparciones de un fragmento de texto
cadena = 'bienvenido a mi aplicación'.capitalize()
print(cadena.count('a'))

# buscar un fragmento de texto dentro de una cadena
print(cadena.find('mi'))
print(cadena.find('mi', 18, 25))