""" El import no solo hace que tengamos disponible todo lo definido dentro 
del módulo, sino que también ejecuta el código del módulo. 
A la hora de importar un módulo Python recorre todos los directorios 
indicados en la variable de entorno PYTHONPATH en busca de un archivo 
con el nombre adecuado. 

Por último es interesante comentar que en Python los módulos también son 
objetos; de tipo module en concreto. Por supuesto esto significa que 
pueden tener atributos y métodos. Uno de sus atributos, __name__, se 
utiliza a menudo para incluir código ejecutable en un módulo pero que 
este sólo se ejecute si se llama al módulo como pro- grama, y no al 
importarlo. Para lograr esto basta saber que cuando se ejecuta el 
módulo directamente __name__ tiene como valor “__main__”, mientras 
que cuando se importa, el valor de __name__ es el nombre del módulo

Otro atributo interesante es __doc__, que, como en el caso de 
funciones y clases, sirve a modo de documentación del objeto 
(docstring o cadena de documentación). Su valor es el de la 
primera línea del cuerpo del módulo, en el caso de que esta 
sea una cadena de texto; en caso contrario valdrá None.
"""

import os, sys  # La clausula import también permite importar varios módulos en la misma línea. 
from time import asctime

import modulo
from otro_modulo import CONSTANTE

import paquete.subpaquete.moduloo

modulo.mi_funcion2()  # imprime: 
                      # un módulo y se muestra siempre
                      # otra funcion 2      

print(asctime())

print(CONSTANTE)  # imprime:
                  # otro_modulo y se muestra siempre
                  # 3

print(sys.path)  # imprime el PYTHONPATH

paquete.subpaquete.moduloo.func()