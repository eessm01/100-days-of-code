""" List Comprehension

En Python 3 map, filter y reduce perderán importancia, 
se desaconsejerán en favor de las list comprehensions.

Está característica consiste en la construcción que 
permite crear listas a partir de otras listas.
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# replace map
l2 = [n ** 2 for n in l]

print(l2)

# replace filter
l3 = [n for n in l if n % 2.0 == 0]
print(l3)

m = [0, 1, 2, 3]
n = ['a', 'b']
# o = [ s * v for s in n
#             for v in m
#             if v > 0]

o = []

for s in n:
    for v in m:
        if v > 0:
            o.append(s * v)

print(o)

