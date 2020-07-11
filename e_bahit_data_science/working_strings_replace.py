"""CIENCIA DE DATOS CON PYTHON by Eugenia Bahit. 2 edition. pages 11-12"""

# dar formato a una cadena, sustituyendo texto dinámicamente
cadena = 'bienvenido a mi aplicación {0}'
print(cadena.format('en Python'))

cadena = 'Importe bruto: ${0} + IVA: ${1} = IMPORTE NETO: {2}'
print(cadena.format(100,21,121))

cadena = 'Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}'
print(cadena.format(bruto=100, iva=21, neto=121))

print(cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21/ 100 + 100))


# remplazar texto en una cadena
buscar = 'nombre apellido'
remplazar_por = 'Juan Pérez'
cadena = 'Estimado Sr. nombre apellido:'.replace(buscar, remplazar_por)
print(cadena)

# eliminar caracteres a la izquierda y derecha de una cadena
cadena = '   www.eugeniahabit.com   '
print(cadena.strip())
cadena = '****www.eugeniahabit.com***'
print(cadena.strip('*'))

# eliminar caracteres a la izquierda de una cadena
cadena = 'www.eugeniahabit.com'
print(cadena.lstrip('w.'))

cadena = '   www.eugeniahabit.com'
print(cadena.lstrip())

# eliminar caracteres a la derecha de una cadena
cadena = 'www.eugeniahabit.com'
print(cadena.rstrip('.com'))

cadena = 'www.eugeniahabit.com       '
print(cadena.rstrip())