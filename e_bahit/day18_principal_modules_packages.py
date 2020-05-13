"""
La importación de módulos debe realizarse al comienzo del documento, en 
orden alfabético de paquetes y módulos.

Primero deben importarse los módulos propios de Python. Luego, los 
módulos de terceros y finalmente, los módulos propios de la aplicación.

Entre cada bloque de imports, debe dejarse una línea en blanco.
"""

import paquete.modulo
from paquete.subpaquete.submodulo import SUBMODULO_CONSTANTE as CONST  # Alias
from paquete.subpaquete.submodulo import funcion_mismo_nombre as fun  # Alias

paquete.modulo.otra_funcion()

print(CONST)

paquete.modulo.funcion_mismo_nombre()

fun()