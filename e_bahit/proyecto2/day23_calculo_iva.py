#-*- coding: utf-8 -*-
"""
1) Cree un script en el que se defina una función que calcule el IVA.
Fórmula aconsejada: bruto + (bruto * alicuota) / 100.0
2) Pida al usuario que ingrese el importe bruto (no olvide usar el hack aprendido)
3) Pida al usuario que ingrese el IVA.
4) Valide el IVA de la siguiente forma:
Si el usuario no indica el IVA, haga que la función utilice uno por defecto (por ejemplo: 10.5).
5) Al finalizar, imprima en pantalla el importe bruto, el neto y la diferencia entre ambos. Sea creativo con los textos así puede utilizar la función format.
6) Haga que tras imprimir, se vuelva a ejecutar todo.
"""
from libs.retrocompatibilidad import echo, get


def get_iva(bruto, alicuota):
    if alicuota:
        neto = (bruto * alicuota) / 100
    else:
        neto = (bruto * 10.5) / 100
    return neto


def get_int(number):
    try:
        return int(number)
    except:
        echo("Por favor, Ingrese un número")
        return None
        

def get_bruto():
    bruto = get("Bruto: ")

    if not bruto or not get_int(bruto):
        bruto = get_bruto()

    return bruto


def get_alicuota():
    default = 10.5
    alicuota = get("Porcentaje de IVA: ")

    if not alicuota:
        echo("Porcentaje default del IVA: {}".format(default))
        return default
    elif not get_int(alicuota):
        return int(alicuota)
         

def run():
    echo(" * * * CALCULO DEL IVA * * * ")
    bruto = int(get_bruto())
    alicuota = get_alicuota()
    iva = get_iva(bruto, alicuota)
    neto = bruto + iva

    echo("Valor BRUTO: {}".format(str(bruto)))
    echo("Valor IVA: {}".format(str(iva)))
    echo("Valor NETO: {}".format(str(neto)))


if __name__ == '__main__':
    while True:
        run()
        word = get("Presione cualquier letra o Q para salir... ")
        if word == 'Q':
            break