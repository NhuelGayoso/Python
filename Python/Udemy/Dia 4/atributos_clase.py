class Persona:

    atributo_clase = 0

    def __init__(self) -> None:
        self.atributo_instancia = 0


print('*** Atributo de clase***')
print(f'Atributo de clase {Persona.atributo_clase}')
# Modificamos el atributo clase
# (Comun a todos los objetos de la clase)
Persona.atributo_clase = 10

# Creamos un objeto
person1 = Persona()
person1.atributo_instancia = 20
print(f'Atributo de clase desde persona1: {person1.atributo_clase}')
print(f'Atributo de instancia desde persona1: {person1.atributo_instancia}')

# Creamos un segundo objeto
person2 = Persona()
person2.atributo_instancia = 30
print(f'Atributo de clase desde persona1: {person2.atributo_clase}')
print(f'Atributo de instancia desde persona1: {person2.atributo_instancia}')
