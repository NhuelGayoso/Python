print('*** Manejo de tuplas ***')
nombres = ('Karla', 'Juan', 'Laura')
print(nombres)

# Creamos una tupla heterogenea
# en las tuplas los parentesis son opcionales
tupla_heterogenea = (100, True, 'Ivonne')
print(tupla_heterogenea)

# Recorrer los elementos de una tupla
for nombre in nombres:
    print(nombre, end=" ")

# Acceder a un elemento
numeros = (100, 200, 300, 400, 500)
print(f'Para el indice 0, el valor es: {numeros[0]}')
print(f'Para el indice 3, el valor es: {numeros[3]}')
print(f'Para el indice -1, el valor es: {numeros[-1]}')

# No podemos modificar las tuplas
# numeros[0] = 1000 manda un error, no podemos modificar elementos de una tupla

numero_a_buscar = 200
if numero_a_buscar in numeros:
    print(f'Si existe {numero_a_buscar} en la tupla')
else:
    print(f'No existe {numero_a_buscar} en la tupla')
