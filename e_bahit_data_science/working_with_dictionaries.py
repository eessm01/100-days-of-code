"""Ciencia de datos con Python 2da. edición.

Manipulación de diccionarios.
"""

# métodos de eliminación
# vaciar un diccionario
diccionario = {
    'color': 'violeta', 
    'talle': 'XS',
    'precio': 174.25
}

print(diccionario)

diccionario.clear()
print(diccionario)

# métodos de agregado y creación
# copiar un diccionario
diccionario = {
    'color': 'violeta', 
    'talle': 'XS',
    'precio': 174.25
}

remera = diccionario.copy()
print(diccionario)
print(remera)

diccionario.clear()
print(diccionario)
print(remera)

musculosa = remera
print(remera)
print(musculosa)

remera.clear()
print(remera)
print(musculosa)

# crear un nuevo diccionario desde las claves de una secuencia
secuencia = ['color', 'talle', 'marca']
diccionario1 = dict.fromkeys(secuencia)
print(diccionario1)

diccionario2 = dict.fromkeys(secuencia, 'valor por defecto')
print(diccionario2)

# concatenar diccionarios
diccionario1 = {'color': 'verde', 'precio': 45}
diccionario2 = {'talle': 'M', 'marca': 'Lacoste'}

print(diccionario1)

diccionario1.update(diccionario2)
print(diccionario2)
print(diccionario1)

# establecer una clave y valor por defecto
# setdefault("clave"[, None|valor_por_defecto])
# Si la clave no existe, la crea con el valor por defecto. Siempre retorna 
# el valor para la clave pasada como parámetro
remera = {'color': 'rosa', 'marca': 'Zara'}
clave = remera.setdefault('talle', 'U')
print(clave)

remera2 = remera.copy()
print(remera2)

clave = remera2.setdefault('estampado')
print(clave)
print(remera2)

clave = remera2.setdefault('marca', 'Lacoste')
print(clave)
print(remera2)

# métodos de retorno
# obtener el valor de una clave 
print(remera.get('color'))
print(remera.get('stock'))
print(remera.get('stock', 'sin stock'))

# saber si una clave existe en el diccionario
existe = 'precio' in remera
print(existe)

existe = 'color' in remera
print(existe)

# obtener las claves y valores de un diccionario
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}

for clave, valor in diccionario.items():
    print(clave, valor)

# claves de un diccionario
for clave in diccionario.keys():
    print(clave)

# obtener las claves en una lista
claves = list(diccionario.keys())
print(claves)

# obtener los valores de un diccionario
for clave in diccionario.values():
    print(clave)

# obtener los valores en una lista
valores = list(diccionario.values())
print(valores)


# obtener la cantidad de elementos de un diccionario
print(len(diccionario))