class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'


if __name__ == '__main__':
    carmen = Persona('Carmen', 40)
    sergio = Persona('Sergio', 39)

    print(carmen.saluda(sergio))
     