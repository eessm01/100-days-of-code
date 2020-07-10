"""Python para todos. Archivos.

Escritura de archivos, para esto se utilizan los métodos
write y writelines.
"""

f = open('write_file_example.txt', 'w')

line = ('Escritura de archivos')
f.write(line)

print(f.tell())

lines = ['Para la escritura de archivos se utilizan los métodos write y writelines.\n',
    'Mientras que el primero funciona escribiendo en el archivo una cadena de texto\n',
    'que toma como parámetro, el segundo toma como parámetro una lista de cadenas de\n',
    'texto indicando las líneas que queremos escribir en el fichero\n'
]

f.writelines(lines)

print(f.tell())

more_lines = ['Hay situaciones en las que nos puede interesar mover el puntero de',
    'lectura/escritura a una posición determinada del archivo. Por ejemplo',
    'si queremos empezar a escribir en una posición determinada y no al final o al principio del archivo.',
    'Para esto se utiliza el método seek que toma como parámetro un número positivo o negativo a utilizar como desplazamiento',
    'También es posible utilizar un segundo parámetro para indicar desde dónde quere- mos que se haga el desplazamiento:',
    '0 indicará que el desplazamiento se refiere al principio del fichero (comportamiento por defecto), 1 se refiere a la',
    'posición actual, y 2, al final del fichero.',
    'Para determinar la posición en la que se encuentra actualmente el puntero se utiliza el método tell(),',
    'que devuelve un entero indicando la distancia en bytes desde el principio del fichero.'
]

for line in more_lines:
    f.write(line+'\n')

print(f.tell())

f.close()