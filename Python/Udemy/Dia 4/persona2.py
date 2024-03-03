class Persona:
    # Variable o atributo de clase
    contador_personas = 0

    # Constructor
    def __init__(self, nombre, apellido):
        # Incrementamos el contador
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'PersonaID: {self.id} nombre: {
              self.nombre} apellido: {self.apellido}')


# Codigo Principal
print('***Ejemplo contador de Objeto***')
persona1 = Persona('Nahuel', 'Gayoso')
persona1.mostrar_persona()
persona2 = Persona('Rocio', 'Cavalle')
persona2.mostrar_persona()