print('*** Cajero Automatico de Ciudad Gotica ***')


salir = False
saldo = 3000.00

while not salir:
    print('''
    Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar
        3. Depositar
        4. Salir''')
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print(f'Su saldo actual es: ${saldo:.2f}\n')

    elif opcion == 2:
        retiro = float(input('Ingresa el monto que deseas retirar: '))
        # Validacion
        if retiro <= saldo:
            saldo -= retiro  # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con saldo suficiente. Saldo actual {saldo}')

    elif opcion == 3:
        deposito = float(input('Ingrese el monto a depositar: '))
        saldo += deposito  # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del cajero automatico. Hasta pronto...')
        salir = True
    else:
        print('Opcion invalida')
