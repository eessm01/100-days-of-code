"""
Si los módulos sirven para organizar el código, los paquetes sirven para 
organizar los módulos. Los paquetes son tipos especiales de módulos 
(ambos son de tipo module) que permiten agrupar módulos relacionados. 
Mientras los módulos se corresponden a nivel físico con los archivos, 
los paquetes se representan mediante directorios.

Para hacer que Python trate a un directorio como un paquete es necesario
crear un archivo __init__.py en dicha carpeta
(es raro, en este ejemplo funcionó sin el archivo __init__.py)
"""


def func():
    print("función que viene de moduloo")


def func2():
    print("función 2 que viene de moduloo")


class Clasee():
    def __init__(self):
        print("constructor de Clasee (moduloo)")


print("Se imprime siempre (paquete.subpaquete.moduloo)")


if __name__ == '__main__':
    print("Esto funciona como un static void main de Java, woow")