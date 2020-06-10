class Instrumento:
    """Abstracción de los objetos instrumento"""
    def __init__(self, precio):
        self.precio = precio
    
    def tocar(self):
        print('Estamos tocando música')
    
    def romper(self):
        print('Esto lo pagas tu')
        print('Son, {} $$$'.format(self.precio))


class Cello(Instrumento):
    pass

class Bateria(Instrumento):
    def __init__(self, num_platillos):
        self.num_platillos = num_platillos


class Guitarra(Instrumento):
    def __init__(self, precio, tipo_cuerda):
        # en este caso es necesario especificar el parámetro self
        Instrumento.__init__(self, precio) 
        self.tipo_cuerda = tipo_cuerda


class Terrestre:
    def desplazar(self):
        print('El animal anda')

    def comer(self):
        print('come animales terrestres')


class Acuatico:
    def desplazar(self):
        print('El animal nada')

    def comer(self, animal):
        print('come animales marinos')


class Cocodrilo(Terrestre, Acuatico):
    """Abstracción de cocodrilo. Herencia multiple.
    
    Como Terrestre se encuentra más a la izquierda,
    sería la definición de desplazar de esta clase la
    que prevalecería.
    """
    # con esta implementacion de cocodrilo
    # Cocodrilo(Acuatico, Terrestre):
    # TypeError: comer() missing 1 required positional argument: 'animal'
    pass

    

if __name__ == '__main__':
    # Si no se pone el valor de precio
    # TypeError: __init__() missing 1 required positional argument: 'precio'
    cello = Cello(450.22)
    print(cello.precio)

    bateria = Bateria(5)
    # print(bateria.precio)
    print(bateria.num_platillos)

    guitarra = Guitarra(1200.99, 'tipo2')
    print(guitarra.precio)
    print(guitarra.tipo_cuerda)


    coco = Cocodrilo()
    coco.desplazar()
    coco.comer()
    
    