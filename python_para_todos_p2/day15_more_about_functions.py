"""
Una función es un fragmento de código con un nombre asociado que
realiza una serie de tareas y devuelve un valor. En python, cuando 
el programador no especifica un valor de retorno la función devuelve
el valor None (nada).

Las funciones ayudan a programar y depurar y reutilizar el código.

En python una función se declara con la palabra def name_function(param)
También podemos encontrarnos con una cadena de texto en la primer linea
del cuerpo de la función (docstring)
"""

def mi_funcion(param1, param2):
    """Esta función imprime los valores pasados como parametros"""
    print(param1)
    print(param2)

mi_funcion("hola",3)
mi_funcion(param2=232,param1="Gatito")


def imprimir(texto,veces=1):
    """También es posible asignar valores por defecto para el caso en el 
    que no se indique ningún valor para ese parámetro al llamar a la función
    """
    print(texto*veces)

imprimir("hola")
imprimir("hola",5)


def varios(param1, param2, *otros):
    """ Es posible definir funciones con un número variables de argumentos,
    para ello colocamos un último parámetro para la funcion, cuyo nombre
    debe precederse con un signo *
    Se crea una tupla con el nombre de "otros"
    """
    for val in otros:
        print(val)
        
varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4, 5)


def varios_dic(param1, param2, **otros):
    """
    """
    for i in otros.items():
        print(i)

varios_dic(1,2,tercero=3)
varios_dic(1,2,tercero=3, cuarto=4, quinto=5)


def f(x,y):
    """
    PASO POR REFERENCIA O POR VALOR.
    referencia - lo que se pasa como argumento la referencia o puntero a la
    variable, es decir, la dirección de memoria.
    por valor - pasa el valor que contenía la variable.

    La diferencia estriba en que en el paso por valor los cambios que se hagan
    sobre el parémetro no se ven fuera de la función

    En C los argumentos de las funciones se pasan por valor, aunque se puede 
    simular el paso por referencia usando punteros.

    En Python, para variables que son objetos, lo que se hace es pasar por
    valor de referencia al objeto. En python todo es un objeto. Para ser exacto,
    lo que ocurre en realidad es que al objeto se le asigna
    otra etiqueta o nombre en el espacio de nombre local de la función.

    Sin embargo, no todos los parámetros que hagamos dentro de la función
    se reflejarían, ya que existen objetos inmutables como las tuplas, por lo
    que si intentáramos modificar una tupla pasada como parámetro lo que
    ocurriría en realidad es que se crearía una nueva instancia. 
    """
    x = x + 3  # los enteros son inmutables
    y.append(23)  # las listas son mutables
    print(x,y)


x = 22
y = [22]
f(x,y)
print(x,y)
# Cómo vemos la variable x no conserva los cambios una vez salimos de la función


def sumar(x,y):
    """ Esta función suma dos valores y el resultado es el valor de retorno.
    """
    return x + y

print(sumar(3,2))


def f2(x,y):
    """ También podemos pasar varios valores que retirnar a return.
        Sin embargo, esto no quiere decir que se puedan regresar varios
        valores realmente, lo que ocurre en realidad es que Python crea
        una TUPLA al vuelo cuyos elementos son los valores a retornar, 
        y esta única variables es la que se devuelve.
    """
    return x * 2, y * 2

a, b = f2(1, 2)
print(a, b)

