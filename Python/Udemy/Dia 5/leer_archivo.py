print('*** leer de informacion de un archivo')
archivo = open('mi_archivo.txt', 'r')  # read -leer
print(archivo.read())
archivo.close()
