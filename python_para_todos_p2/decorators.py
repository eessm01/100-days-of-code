"""Python para todos. Decorators

Un decorador no es mas que una función que recibe
una función como parámetro y devuelve otra función
como resultado.

Los decoradores se ejecutan de abajo a arriba
"""


def mi_decorador(funcion):
    def nueva_funcion(*args):
        print('Llamada a la funcion {}"'.format(
            funcion.__name__
        ))
        return funcion(*args)
    return nueva_funcion


@mi_decorador
def imp(s):
    print(s)


# sin poner la línea @mi_decorador 
# mi_decorador(imp)('hola')

imp('hola')


@mi_decorador
def imp(s):
    print(s)


def other_decorator(func):
    def wrapper(*args):
        print('Este es otro decorador, antes de la funcion')
        func(*args)
        print('Este es otro decorador, despues de la funcion')
    return wrapper


@mi_decorador
@other_decorator
def say_hello(s):
    print(s)


say_hello('hi')

# @other_decorator
# @mi_decorador
# Este es otro decorador, antes de la funcion
# Llamada a la funcion say_hello"
# hi
# Este es otro decorador, despues de la funcion

# @mi_decorador
# @other_decorator
# Llamada a la funcion wrapper"
# Este es otro decorador, antes de la funcion
# hi
# Este es otro decorador, despues de la funcion