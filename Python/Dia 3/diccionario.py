print('*** Manejo de diccionarios ***')
# Un diccionario almacena sus elementos en forma de llave:valor, y ademas no se pueden duplicar sus elementos
diccionario = {
    'nombre': 'Nahuel',
    'apellido': 'Gayoso',
    'edad': 29,  # el valor se omite
    'edad': 30,  # nos quedamos con el ultimo valor definido
}

print(diccionario)

# Acceder a los elementos
print(f'Nombre: {diccionario["nombre"]}')
print(f"Apellido: {diccionario['apellido']}")
print(f'Edad: {diccionario.get('edad')}')

# El largo de un diccionario
print(f'El largo del diccionario: {len(diccionario)}')

# Agreagar elementos a un diccionario
diccionario['telefono'] = 50255786
print(f'Diccionario modificado: {diccionario}')

# Obtener una lista de las llaves del diccionario
print(f'Lista de las llaves del dic: {diccionario.keys()}')

# Obtener una lista de los valores del diccionario
print(f'Lsta de los valores del dic: {diccionario.values()}')

# Obtener los elementos del dic (items)
print(f'Lsta de los valores del dic: {diccionario.items()}')

# Revisar si existe una llave en el diccionario
llave_a_buscar = 'nombre'
if llave_a_buscar in diccionario:
    print(f'La llave {llave_a_buscar} si existe en el diccionario')
else:
    print(f'La llave {llave_a_buscar} no existe en el diccionario')

# Actualizar un elemento del dic
diccionario['edad'] = 30
print(f'Nuevo dic: {diccionario}')

# Eliminar un elemento del diccionario
diccionario.pop('telefono')
print(f'Nuevo dic: {diccionario}')

# Recorrer las llaves de un dic(keys)
for llave in diccionario.keys():
    print(llave)

# Recorrer los valores de un dic(values)
print()
for valor in diccionario.values():
    print(valor)

# Recorrer los elementos de un diccionario como tupla
print()
for llave, valor in diccionario.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Limpiar el dic
diccionario.clear()
print(f'Diccionario limpio: {diccionario}')
