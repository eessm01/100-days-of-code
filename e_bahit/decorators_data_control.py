def get_post_data(funcion):  # decorador

    def wrapper(environ):  # claramente este es el wrapper del decorador
        _POST = {}

        try:
            datos = environ['wsgi.input'].read().split('&')
            for par in datos:
                key, value = par.split('=')
                _POST[key] = unquote(value).replace('+',' ')
                key, value = (None, None)
        except:
            pass

        return function(_POST)

    return wrapper


@get_post_data
def guardar(POST):
    nombre = POST['nombre']
    apellido = POST['apellido']


@get_post_data
def actualizar(POST):
    pass


@get_post_data
def eliminar(POST):
    pass