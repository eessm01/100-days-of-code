"""Ejemplo sobre scope en Python
"""

def funcion1(un_argumento, una_funcion):
    def funcion2(otro_argumento):
        return otro_argumento * 2
    
    valor = funcion2(un_argumento)
    return una_funcion(valor)


un_argumento = 1

def cualquier_funcion(cualquier_argumento):
    return cualquier_argumento + 5


resultado = funcion1(un_argumento, cualquier_funcion)
print(resultado)