
# coding= UTF-8
"""
La función map aplica una función a cada elemento de la secuencia y devuelve
una lista con el resultado de aplicar la función a cada elemento. Si se 
pasan como parámetros n secuencias, la función tendrá que aceptar n argumentos
Si alguna secuencias es más pequeña que las demás, el valor que le llega a la
función function para posiciones mayores que el tamaó de dicha secuenca será 
None.

La función filter verifica que los elementos de una secuencia cumplan una 
determinada condición, devolviendo una secuencia con los elementos que 
cumplen esa condición. Es decir, para cada elemento de sequence se aplica la 
función function; si el resultado es True, se añade a la lista y en caso 
contrario se descarta.

La función reduce aplica a una función a pares de elementos de una secuencia
hasta dejarla en un solo valor.
"""

# map
def cuadrado(n):
    return n ** 2

l = [1, 2 ,3, 4, 5]
l2 = map(cuadrado, l)

for e in l2:
    print(e)

# filter
def es_par(n):
    return (n % 2.0 == 0)

l3 = filter(es_par, l)

for e in l3:
    print(e)


# reduce
# sólo existe en python2
def sumar(x, y):
    return x + y

valor = reduce(sumar, l)

print(valor)

otro_valor = reduce(lambda x, y: x*y, l)

print(otro_valor)