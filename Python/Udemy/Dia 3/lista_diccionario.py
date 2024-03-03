print('*** Lista y Diccionario')

personas = [{
    'nombre': 'Nahuel',
    'apellido': 'Gayoso',
    'edad': 29,
}, {
    'nombre': 'Rocio',
    'apellido': 'Cavalle',
    'edad': 37,
}]

print(personas)

# Accedera un diccionario (persona)
print(personas[1])

# Acceder a un valor (llave) nombre del primero elemento
print(personas[0].get('nombre'))
print(personas[1].get('nombre'))

# Recorrer los elementos de las listas (elemento = diccionario)
for contador, persona in enumerate(personas):  # funcion enumerate()
    print(f'Persona: {contador}: {persona.get('apellido')}')
