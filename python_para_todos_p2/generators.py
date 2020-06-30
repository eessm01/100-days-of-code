"""Python para todos. Generators

Funcionan de forma similar a las list comprehensions
Su sintexis es igual, excepto porque usan parántesis
en lugar de corchetes.

Sin embargo, NO devuelven una lista, sino un generador.
Un GENERADOR genera valores sobre los que iterar.

Como no se crea una lista en memoria, sino que se genera
un valor cada vez que se necesita, el uso de generadores
puede suponer una gran diferencia de memoria.

En todo caso, siempre es posible crear una lista a partir
de un generador
                lista = list(mi_generador)
"""

l = [1, 2, 3]
l1 = [n ** 2 for n in l]
print(l1)
l2 = (n ** 2 for n in l)
print(l2)


def mi_generador(n, m, s):
    while(n <= m):
        yield n
        n += s

g = mi_generador(0, 5, 1)
print(g)

for e in mi_generador(0, 5, 1):
    print(e)