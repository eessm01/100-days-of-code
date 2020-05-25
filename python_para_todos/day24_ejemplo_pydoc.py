"""Modulo para ejemplificar el uso de pydoc."""

class Persona:
    """Mi clase de ejemplo."""
    def __init__(self, nombre):
        """Inicializador de la clase persona."""
        self.nombre = nombre
        self.mostrar_nombre()

    def mostrar_nombre(self):
        """Imprime el nombre de la persona"""
        print "Esta es la persona {}".format(self.nombre)

class Empleado(Persona):
    """Subclase de persona."""
    pass

if __name__ == '__main__':
    raul = Persona("Raul")

    # para generar un html
    # pydoc -w day23_ejemplo_pydoc 