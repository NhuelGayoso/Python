print('*** Argumentos variables ***')


def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'SuperHeroe: {nombre} - {args}. Mas info: {kwargs}')
    for superpoder in args:
        print(F'Superpoder: {superpoder}')


# Llamamos a la funcion
superheroe_superpoderes('Spiderman', 'Instinto aracnido',
                        'Telaraña', edad=17, empresa='Marvel')
superheroe_superpoderes('Iron Man', 'Armadura', 'Playboy', 'Millonario')
# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino')
