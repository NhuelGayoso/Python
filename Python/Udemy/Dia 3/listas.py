print('*** Listas en Python ***')
nombres = ['Karla', 'Juan', 'Laura']
print(f'Lista de nombre: {nombres}')

# Lista heterogenea (multiples tipos datos)
lista_heterogenea = [100, True, 'Ivonne']
# print(f'Lista heterogenea: {lista_heterogenea}')

# Iterar los elementos de una lista
for nombre in nombres:
    print(nombre)

# Listas de numeros (leer o acceder a los elementos o valores de una lista)
numeros = [100, 200, 300, 400, 500]

# Recuperar sus elementos por indice
print(f'Para el indice 0, recuperamos el valor: {numeros[0]}')
print(f'Para el indice 3, recuperamos el valor: {numeros[3]}')

# Modificar los elementos de una lista
numeros[0] = 1000
numeros[1] = 2000
print(f'Lista modificada: {numeros}')

# Preguntar si un valor existe en mi lista
numero_a_buscar = 1000
if numero_a_buscar in numeros:
    print(f'Si existe {numero_a_buscar} en mi lista')
else:
    print(f'No existe {numero_a_buscar} en mi lista')
# Recuperar el indice de cierto elemento
indice = numeros.index(numero_a_buscar)
print(f'El indice del numero {numero_a_buscar} es: {indice}')

# Redifinir la lista
numeros = [100, 200, 300, 400, 500]

# Recuperar una sublista. lista[indice_inicio:indice_final - 1]
valores_recuperados = numeros[0:3]  # se recupera: [0:2]
print(valores_recuperados)

# Recuperar una sublista indica indice final
valores_recuperados = numeros[:2]
print(valores_recuperados)

# Recuperar una sublista indicando indice inicial
valores_recuperados = numeros[3:]
print(valores_recuperados)

# Realizar una copia
lista_copiada = numeros[:]
# numeros[0] = 1000  # Son listas distintas en memoria
print(f'Lista original: {numeros}')
print(f'Lista copiada: {lista_copiada}')

# Metodos de listas
largo_lista = len(numeros)
print(f'Largo de lista: {largo_lista}')

# Agregar un nuevo elemento. append Agrega el nuevo elemento al final
numeros.append(600)
print(f'Lista con un nuevo valor agregado con append: {numeros}')

# Insertar nuevos elementos, en el indice indicado
numeros.insert(1, 150)
print(f'Lista con un nuevo valor en el indice 1: {numeros}')

# Eliminar un valor de una lista
numeros.remove(400)
print(f'Lista con elemento eliminado: {numeros}')

# Concatenar lista
lista_nueva = numeros + lista_copiada
print(f'Lista concatenada: {lista_nueva}')

# Eliminar un elemento por indice
del numeros[3]  # removepor indice
print(f'Lista sin el valor del indice 3: {numeros}')

# Eliminar la lista completa
numeros[:] = []
print(f'La lista de numero esta vacia')

# Eliminar por completo la variabilidad
del numeros
print(numeros)
