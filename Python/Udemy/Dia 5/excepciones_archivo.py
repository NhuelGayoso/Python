print('*** Excepciones y Archivos ***')
nombre_archivo = 'mi_archivo.txt'
archivo = None
try:
    archivo = open(nombre_archivo, 'a+')
    try:
        archivo.write('Nuevo contenido...')
    except Exception as e:
        print(f'Error  al escribir al archivo {e}')
except Exception as e:
    print(f'Error al abrir archivo {e}')
else:
    print(f'se abrio correctamente el archivo:{nombre_archivo}')
finally:
    print('Termina programa...')
    if archivo is not None:
        archivo.close()
    else:
        print('La variable de archivo no se inicializo... ')
