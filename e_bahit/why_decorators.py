"""The Original Hacker N.4. Wrappers y Decoradores.

¿Para que usaríamos un wrapper?

los wrappers o envolturas, suelen utilizarse cuando se tienen
funciones que antes de ejecutar su verdadera funcionalidad, 
realizan acciones redundantes. Un ejemplo muy típico, es
cuando se utilizan bloques try y except
"""

# def get_template():
#     try:
#         with open('template.html','r') as archivo:
#             return archivo.read()
#     except:
#         return 'ERROR INTERNO'

# def calcular(partes=0, total=100):
#     try:
#         return total/partes
#     except:
#         return 'ERROR INTERNO'

# Como podemos ver, tenemos dos funciones que utilizan bloques 
# try y except (generalmente, se tienen muchísimas más). 
# Una forma de manejar los errores en estas funciones, 
# sería utilizar un wrapper

def intentar(funcion):
    # Usamos * args y **kwargs ya que tenemos una función que necesita argumentos
    def wrapper(*args, **kwargs):
        try:
            return funcion(*args, **kwargs)
        except:
            return 'ERROR INTERNO'
    
    return wrapper


@intentar
def get_template():
    with open('','r') as archivo:
        return archivo.read()


@intentar
def calcular(partes=0, total=100):
    return total/partes


resultado = calcular()
print(resultado)