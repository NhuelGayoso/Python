print('*** Regresar una tupla de valores desde una funcion ***')

# definicion de la funcion


def persona_mayuscula(nombre, apellido, edad):
    print('Esta funcion regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)


# programa principal
nombre, apellido, edad = persona_mayuscula('Nahuel', 'Gayoso', 29)
print(f'Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}')
