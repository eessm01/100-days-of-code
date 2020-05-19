"""
El concepto de funciones de orden superior se refiere al uso de funciones
como si de un valor cualquiere se tratara, posibilitando el pasar 
funciones como parámetros de otras funciones o devolver funciones como 
valor de retorno. Esto es posible porque en Python, todo son objetos.
"""

def saludar(lang):
    def saludar_es():
        print("Hola")
    
    def saludar_en():
        print("Hi")
    
    def saludar_fr():
        print("Salut")

    lang_func = {"es": saludar_es,
                 "en": saludar_en,
                 "fr": saludar_fr}
    
    return lang_func[lang]


# forma 1 de ejecutar 
f = saludar("es")
f()

# segunda forma de ejecutar
saludar("fr")()