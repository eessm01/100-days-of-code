class Coche:
    """Abstraccion de los objetos coche
    
    For the name of the class using CamelCase notation.
    """
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print('Tenemos {} litros'.format(self.gasolina))

    def arrancar(self):
        if self.gasolina > 0:
            print('Arranca')
        else:
            print('No Arranca')
    
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print('Quedan {} litros'.format(self.gasolina))
        else:
            print('No se mueve')


if __name__ == '__main__':
    mi_coche = Coche(3)

    print(mi_coche.gasolina)
    mi_coche.arrancar()
    mi_coche.conducir()
    mi_coche.conducir()
    mi_coche.conducir()
    mi_coche.conducir()
    mi_coche.arrancar()