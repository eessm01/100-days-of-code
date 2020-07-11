"""CIENCIA DE DATOS CON PYTHON by Eugenia Bahit. 2 edition. pages 9-11"""

# unir una cadena de forma iterativa
formato_numero_factura = ("No 0000-0", "-0000 (ID: ", ")")
numero = "275"
numero_factura = numero.join(formato_numero_factura)
print(numero_factura)

# partir una cadena en tres partes, utilizando un separador
tupla = 'http://www.eugeniabahit.com'.partition('www.')
print(tupla)

protocolo, separador, dominio = tupla
cadena = 'Protocolo: {0}\nDominio: {1}'.format(protocolo, dominio)
print(cadena)

# partir una cadena en varias partes utilizando un separador
keywords = 'python, guia, curso, tutorial'.split(', ')
print(keywords)

# partir una cadena en líneas
texto = """Linea 1
Linea 2, bla, bla, bla
Linea 3
Linea 4
"""
print(texto.splitlines())
texto = 'Linea 1\nLinea 2\nLinea 3'
print(texto.splitlines())