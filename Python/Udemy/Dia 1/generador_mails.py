print('### Bienvenido al sistema de generacion de email de ciudad Gotica ###')

nombre = input('Cual es tu nombre?: ')
apellido = input('Cual es tu apellido?: ')

email = f'{nombre.lower()}.{apellido.lower()}@ciudadgotica.com'

print(f'''
    Tu nuevo email generado por el sistema es :
    {email}
    *** Felicidades ****''')
