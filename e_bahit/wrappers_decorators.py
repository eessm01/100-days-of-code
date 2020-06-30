"""The Original Hacker. N.4. Wrappers y Decoradores.

Closure. Es una función que dentro de ella contiene a
otra función la cual es retornada cuando el closure es
invocado.

DECORADOR. Es aquel closure que cómo parámetro recibe
una función (llamada función "decorada") cómo único
argumento.

WRAPPER. No es más que la función interna de un closure
que a la vez sea de tipo decorador. LA FUNCION DECORADA
deberá ser INVOCADA por el wrapper

El decorador no se invoca como una función normal. 
Éste es llamado con una sintaxis especial:

@decorador

La sintaxis anterior se debe colocar en la línea anterior 
a la definición de la función decorada. De esta forma, 
el nombre de la función decorada es pasado como parámetro 
de forma automática sin tener que invocar nada más
"""

def closure(parametro1):
    def funcion(parametro2):
        print(parametro1 + parametro2)
    return funcion

foo = closure(10)

foo(200)  # imprime 210
foo(500)  # imprime 510


def decorador(funcion_decorada):

    def funcion():
        pass
    return funcion




def decorador2(funcion_decorada):

    def wrapper():
        pass

    return wrapper


def decorador3(fucion_decorada):

    def wrapper():
        return fucion_decorada()

    return wrapper


@decorador3
def funcion_decorada():
    print("Soy una función decorada")
