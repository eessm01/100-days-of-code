"""The Original Hacker No.3. Funciones Lambda.

Es una forma de definir una función de una SOLA intrucción
en una SOLA línea de código.

variable = lambda param1, param2, paramn: intrucción a ser retornada
"""

mi_funcion = lambda nombre: 'Hola {}'.format(nombre.upper())

print(mi_funcion('carmen'))

neto = lambda bruto, iva=21: bruto + (bruto * iva / 100)

print(neto(100))

print(neto(200))

print(neto(100, 19))

# neto es una variable del tipo 'function lambda'
print(neto)