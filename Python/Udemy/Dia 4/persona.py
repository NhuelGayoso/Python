class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self._nombre = nombre  # Atributo protegido (encapsulamiento)
        self.__apellido = apellido  # Atributo privado

    def mostrar_persona(self):
        print(f'Persona: nombre = {
              self._nombre}, apellido = {self.__apellido}')

    def get_nombre(self):  # Para leer la informacion
        return self._nombre

    def set_nombre(self, nombre):  # Para modificar la informacion
        self._nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido


# Codigo Principal
persona1 = Persona('Nahuel', 'Gayoso')
# persona1.mostrar_persona()
print(persona1.get_nombre())
print(persona1.get_apellido())

# Modificar los valores de los atributos
persona1.set_nombre('Norberto')
persona1.set_apellido('Ibañez')
persona1.mostrar_persona()
# Accedemos a los atributos directamente (publicos)
# persona1.nombre = 'Rocio'
# print(persona1._nombre)  # Esto no es buena practica
# print(persona1.__apellido)  # No podemos acceder el atributo privado
# persona1.apellido = 'Cavalle'
# persona1.mostrar_persona()
