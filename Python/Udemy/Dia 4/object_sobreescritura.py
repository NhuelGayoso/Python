class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    # Sobreescribir el metodo __str__

    def __str__(self) -> str:
        return f'''Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. Mem. {super.__str__(self)}
        '''


# Codigo Principal
persona1 = Persona('Nahuel', 'Gayoso')
print(persona1)
