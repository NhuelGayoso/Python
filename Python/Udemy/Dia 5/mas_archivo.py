print('*** Leer lineas de un archivo***')
nombre_archivo = 'mi_archivo.txt'
archivo = open(nombre_archivo)  # por default se abre en modo lectura

# Leer las lineas del archivo
for linea in archivo:
    print(linea)
archivo.close()

# Volvemos a abrir el archivo
archivo = open(nombre_archivo)
lineas = archivo.readline()
for linea in lineas:
    print(linea)
archivo.close()

# Abrir el archivo como recurso (with)
with open(nombre_archivo) as archivo:
    print(archivo.read())