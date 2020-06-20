class Autommovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)
        self._limpiaparabrisas = LimpiaParabrisas()

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento'

    def lavar_parabrisas(velocidad):
        self._limpiaparabrisas.encender(velocidad)



class Motor():

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass


class LimpiaParabrisas():

    def __init__(self):
        self._estado = 'en reposo'
        self.velocidad = 0

    def encender(self, velocidad):
        self.velocidad = velocidad
        self._estado = 'en movimiento'
