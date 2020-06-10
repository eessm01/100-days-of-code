class Ejemplo:
    def publico(self):
        print('Publico')

    def __privado(self):
        """Método privado

        los nombres que comienzan con un doble guion bajo
        se renombran para incluir el nombre de la clase.
        name mangling
        """
        print('Privado')


class Fecha():
    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia
    
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print('Error')


# Python 2.x Class Definition:
class Persona(object):
    def __init__(self):
        self.__edad = 0

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        if edad > 0 or edad < 120:
            self.__edad = edad
        else:
            print('Algo anda mal')

    edad = property(getEdad, setEdad)


if __name__ == '__main__':
    ej = Ejemplo()
    ej.publico()
    # AttributeError: 'Ejemplo' object has no attribute '__privado'
    # ej.__privado()
    ej._Ejemplo__privado()  # name mangling

    mi_fecha = Fecha()
    print(mi_fecha.getDia())
    mi_fecha.setDia(28)
    print(mi_fecha.getDia())

    # AttributeError: 'Fecha' object has no attribute '__dia'
    # print(mi_fecha.__dia)
    print(mi_fecha._Fecha__dia)  # name mangling


    persona = Persona()
    print(persona.getEdad())
    persona.setEdad(22)
    print(persona.getEdad())
    print(persona._Persona__edad)
    print(persona.__str__)


