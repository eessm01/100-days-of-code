class Coordenada:
    """Abstracción de un punto
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        """Get distance between this point and other point.

        We can help with this Pythagoras.
        c**2 = a**2 + b**2
        c is the distance
        a = it's length of side a
        b = it's length of side b
        """
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_1, Coordenada))

