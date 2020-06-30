"""The Original Hacker No.3. Closures

Un closure es una función que define otra
función y la retorna al ser invocado.

Un closure DEBE tener una razón de ser. De hecho, mi consejo
es evitarlos toda vez que sea posible resolver el planteo sin 
utilizarlos. Pues dificulta la lectura del código y su 
entendimiento, cuando en realidad, debería estar ahí para 
facilitarlo.

Se justifica el uso de closures cuando su finalidad consista
en evitar la redundancia y la sobrecarga de parámetros.

La MEJOR IMPLEMENTACIÓN de un closure no será la que haya 
sido perfectamente planificada sobre un papel en blanco, sino
aquella alcanzada tras un cuidadoso refactoring.
"""

def closure1():

    def funcion_interna():
        return 1
    
    return funcion_interna


variable1 = closure1()
print(variable1())


def closure2(parametro):

    def funcion():
        return parametro + 1  # parametro es de la función closure2()

    return funcion


variable2 = closure2(parametro=1)
print(variable2())


# Un ejemplo bien implementado
def calcular_iva(alicuota):

    def estimar_neto(importe_bruto):
        return importe_bruto + (importe_bruto * alicuota / 100)
    
    return estimar_neto

# Productos gravados con el 21%
get_neto_base_21 = calcular_iva(21)
harina = get_neto_base_21(10)
arroz = get_neto_base_21(8.75)
azucar = get_neto_base_21(21.5)

# Productos gravados con el 10.5
get_neto_base_105 = calcular_iva(10.5)
tv = get_neto_base_105(12700)
automovil = get_neto_base_105(73250)

# El requerimiento anterior, podría haber requerido definir dos 
# funciones independientes (get_neto_base_21 y get_neto_base_105)
# con prácticamente el mismo algoritmo y una importante redundancia.

# En su defecto, podría haberse resuelto mediante una única función
# con 2 parámetros, la cual hubiese requerido replicar el valor de 
# uno de los parámetros incansablemente, en las reiteradas llamadas.


# Otras opciones
# redundancia de funciones
def get_neto_base_21(importe_bruto):
    return importe_bruto + (importe_bruto * 21 / 100)   # linea redundante

def get_neto_base_105(importe_bruto):
    return importe_bruto + (importe_bruto * 10.5 / 100) # linea redundante

harina = get_neto_base_21(10)
arroz = get_neto_base_21(8.75)
azucar = get_neto_base_21(12.5)
tv = get_neto_base_105(12700)
automovil = get_neto_base_105(73250)

# redundancia de parámetros
def get_neto(alicuota_iva, importe_bruto):
    return importe_bruto + (importe_bruto * alicuota_iva / 100)

harina = get_neto(21, 10)
arroz = get_neto(21, 8.75)
azucar = get_neto(21, 12.5)

tv = get_neto(10.5, 12700)
tv = get_neto(10.5, 73250)

# qué pasaría con 1000 productos??