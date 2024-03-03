print('*** Funcion por argumentos por nombres ***')


def crear_persona(nombre, apellido=' ', edad=0):
    print(f'Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}')


# Llamamos a la funcion
# crear_persona('Nahuel', 'Gayoso', 29)

# Llamar a la funcion argumentos por nombre
crear_persona(edad=29, nombre='Nahuel')
