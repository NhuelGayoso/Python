# Menu interactivo con el ciclo while
print('*** Sistema de Administracion de cuentas ***')
salir = False
while not salir:
    opcion = int(input('''
    Menu:
        1. Crear cuenta
        2. Eliminar cuenta
        3. Salir
    Escoja una opcion: '''))
    if opcion == 1:
        print('Creando cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto...')
        salir = True
