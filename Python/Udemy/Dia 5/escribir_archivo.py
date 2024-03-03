print('*** Escribir informacion a un archivo')
archivo = open('mi_archivo.txt', 'w')  # write - escribir
archivo.write('Hola mundo\n')
archivo.close() # Cerramos el buffer