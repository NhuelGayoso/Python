import os

# Escrbir una lista de datos a un archivo

nombre_archivo = 'mi_archivo.txt'
lista = ['Global\n', 'Mentoring\n']
with open(nombre_archivo, 'a+') as archivo:
    archivo.writelines(lista)
print('Se anexo la lista  de datos')

# Eliminar un archivo
os.remove(nombre_archivo)
print('Se elimino nombre archivo')
