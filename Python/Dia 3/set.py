print('*** Manejo de set en Python ***')
# un set es un conjunto de datos no ordenado y no se puede repetir sus elementos
conjunto = {'Karla', 100, 'Laura', True, 'Karla'}
print(conjunto)

# conjunto[0] = 'Karla2' arroja error, no se pueden modificar los elementos

for elemento in conjunto:
    print(elemento, end=' ')

numero_a_buscar = 100
if numero_a_buscar in conjunto:
    print(f'Si existe {numero_a_buscar} en la set')
else:
    print(f'No existe {numero_a_buscar} en la set')

# length - Largo
largo = len(conjunto)
print(f'La cantidad de elementos en mi set se: {largo}')

# Eliminar un elemento
conjunto.remove(100)
print(conjunto)

# Agregar nuevos elementos
conjunto.add(600)
print(conjunto)
