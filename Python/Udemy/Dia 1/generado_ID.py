from random import randint

print('### Sistema Generador de ID ###')

nombre = input("Cual es tu Nombre?: ")
apellido = input("Cual es tu Apellido?: ")
nacimiento = input("Cual es tu Año de Nacimiento (YYYY)?: ")

nombre_id = nombre[:2].upper()  # print(nombre_id.upper())
apellido_id = apellido[0:2]
nacimiento_id = nacimiento[2:4]
print(nacimiento_id)

# Generar un valor de 4 digitos aleatoria
aleatoria = randint(0, 9999)

# Id unico
id_unico = f'{nombre_id}{apellido_id}{nacimiento_id}{aleatoria}'

print(f'''\nHola {nombre}, habitante de ciudad gotica!
    Tu nuevo numero de ID generado por el sistema es:
    {id_unico}
    Felicidades!
    ''')
