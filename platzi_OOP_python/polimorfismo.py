class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} anda caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    # sobre escribe el método
    def avanza(self):
        print(f'{self.nombre} anda en su bicicleta')


def main():
    persona = Persona('Juan')
    persona.avanza()

    ciclista = Ciclista('Monica')
    ciclista.avanza()

if __name__ == "__main__":
    main()