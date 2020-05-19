"""
El operador lambda sirve para crear funciones anónimas en línea. 
Al ser funciones anónimas, es decir, sin nombre, estás no podrán 
ser referenciadas más tarde.

    lambda parameter_list: expression

Las funciones lambda están restringidas por la sintaxis a una sola
expresión.
"""

l = [1, 2, 3, 4, 5]
l2 = filter(lambda n: n % 2.0 == 0, l)

for e in l2:
    print(e)