#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Una variable se <<inyecta>> en una cadena de texto haciendo que su valor pase a
formar parte de la cadena. Esto se hace mediante una operación de formato.
Esto es necesario cuando la cadena a ser inyectada debe contener datos que son
variables.

Para inyectar variables dentro de una cadena, las cadenas deben ser preparadas
mediante el uso de modificadores. Un modificador puede ser un par de llaves
vacias {} 

cadena.format(variable1, variable2)

o un par de llaves con nombre.

cadena.format(dato1=variable1, dato2=variable2)

'Introducción al lenguaje Python' pag 45.

Observación.
print 'a{2} b{1} c{2}'.format(1,2,3)
imprime:
a3 b2 c3
"""

variable1 = 'Pepito'
variable2 = 13

# cadena con modificadores
cadena = "Cadena preparada para recibir dos datos variables: {} y {}"

resultado = cadena.format(variable1, variable2)

print(resultado)

# cadena con modificadores con valor
cadena = "Cadena preparada para recibir dos datos variables: {dato1} y {dato2}"

resultado = cadena.format(dato1=variable1, dato2=variable2)

print(resultado)


