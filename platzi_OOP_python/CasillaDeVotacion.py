class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError('La region {} no es valida en {}'.format(
                region, 
                self._pais
            ))


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
    print(casilla.region)

    casilla.region = 'Morelos'
    print(casilla.region)