import os
class CatalogoPeliculas:
    nombre_archivo = 'pelicula.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_pelicula(cls):
        with open(cls.nombre_archivo, 'r', encoding='utf-8') as archivo:
            print('*** Listado de peliculas ***')
            print(archivo.read())

    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.nombre_archivo)
        print(f'Archivo eliminado: {cls.nombre_archivo}')
