
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/2


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self.base * self.altura
        

if __name__ == "__main__":
    rectangulo = Rectangulo(3, 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())
    