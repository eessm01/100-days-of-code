class Usuario:

    def __init__(self, nombre, clave):
        self.nombre = nombre
        # protected
        self._clave = clave
        # private
        self.__pass = clave  # name mangling



if __name__ == "__main__":
    usuario = Usuario('Roberto','querty')
    print('{} {}'.format(usuario.nombre, usuario._clave))

    print('{} {}'.format(usuario.nombre, usuario.__pass))