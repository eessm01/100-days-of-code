"""CIENCIA DE DATOS CON PYTHON by Eugenia Bahit. 2 edition. pages 9-11"""

# saber si una cadena comienza con un fragmento de texto
cadena = 'bienvenido a mi aplicación'.capitalize()
print(cadena.startswith('Bienvenido'))
print(cadena.startswith('aplicación'))
print(cadena.startswith('aplicación', 16))

# saber si una cadena finaliza con un fragmento de texto
cadena = 'bienvenido a mi aplicación'.capitalize()
print(cadena.endswith('aplicación'))
print(cadena.endswith('Bienvedido'))
print(cadena.endswith('Bienvedido', 0, 10))

# saber si una cadena es alfanumerica
cadena = 'pepegrillo 75'
print('"{}" ¿es alfanumérica? {}'.format(
    cadena,
    cadena.isalnum())
)

cadena = 'pepegrillo'
print('"{}" ¿es alfanumérica? {}'.format(
    cadena,
    cadena.isalnum())
)

cadena = '75'
print('"{}" ¿es alfanumérica? {}'.format(
    cadena,
    cadena.isalnum())
)

cadena = 'pepegrillo75'
print('"{}" ¿es alfanumérica? {}'.format(
    cadena,
    cadena.isalnum())
)

# saber si una cadena es alfabética
cadena = 'pepegrillo 75'
print('"{}" ¿es alfabética? {}'.format(
    cadena,
    cadena.isalpha())
)

cadena = 'pepegrillo'
print('"{}" ¿es alfabética? {}'.format(
    cadena,
    cadena.isalpha())
)

cadena = 'pepegrillo75'
print('"{}" ¿es alfabética? {}'.format(
    cadena,
    cadena.isalpha())
)

# saber si una cadena es numérica
cadena = 'pepegrillo 75'
print('"{}" ¿es dígito? {}'.format(
    cadena,
    cadena.isdigit())
)

cadena = '75589'
print('"{}" ¿es dígito? {}'.format(
    cadena,
    cadena.isdigit())
)

cadena = '755 89'
print('"{}" ¿es dígito? {}'.format(
    cadena,
    cadena.isdigit())
)

cadena = '75.89'
print('"{}" ¿es dígito? {}'.format(
    cadena,
    cadena.isdigit())
)

# saber si una cadena contiene sólo minúsculas
cadena = 'pepe grillo'
print('"{}" ¿contiene sólo minúsculas? {}'.format(
    cadena,
    cadena.islower()
))

cadena = 'Pepe Grillo'
print('"{}" ¿contiene sólo minúsculas? {}'.format(
    cadena,
    cadena.islower()
))

cadena = 'Pepegrillo'
print('"{}" ¿contiene sólo minúsculas? {}'.format(
    cadena,
    cadena.islower()
))

cadena = 'pepegrillo 75'
print('"{}" ¿contiene sólo minúsculas? {}'.format(
    cadena,
    cadena.islower()
))

# saber si una cadena contiene sólo mayúsculas
cadena = 'PEPE GRILLO'
print('"{}" ¿contiene sólo mayúsculas? {}'.format(
    cadena,
    cadena.isupper()
))

cadena = 'PEPE GRILLO 89798'
print('"{}" ¿contiene sólo mayúsculas? {}'.format(
    cadena,
    cadena.isupper()
))

cadena = 'PEPE GRiLLO'
print('"{}" ¿contiene sólo mayúsculas? {}'.format(
    cadena,
    cadena.isupper()
))

cadena = 'PEPEGRILLO'
print('"{}" ¿contiene sólo mayúsculas? {}'.format(
    cadena,
    cadena.isupper()
))

# saber si una cadena contiene solo espaciones en blanco
cadena = '     o'
print('"{}" ¿contiene sólo espacios en blanco? {}'.format(
    cadena,
    cadena.isspace()
))

cadena = '       '
print('"{}" ¿contiene sólo espacios en blanco? {}'.format(
    cadena,
    cadena.isspace()
))

# saber si una cadena tiene formato de título
cadena = 'Pepe Grillo'
print('"{}" ¿es un título? {}'.format(
    cadena,
    cadena.istitle()
))

cadena = 'Pepe grillo'
print('"{}" ¿es un título? {}'.format(
    cadena,
    cadena.istitle()
))

cadena = 'Pepe es Grillo'
print('"{}" ¿es un título? {}'.format(
    cadena,
    cadena.istitle()
))