print('*** Calculadora en Pyhton ***')
print('Operaciones a realizar: ')
salir = False
while not salir:
    print('''
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    ''')
    opcion = int(input('Escoje una opcion: '))
    # Operaciones
    if opcion == 1:
        valor1 = float(input('Dame el valor 1: '))
        valor2 = float(input('Dame el valor 2: '))
        suma = valor1 + valor2
        print(f'El resultado de la suma es: {suma}')
    elif opcion == 2:
        valor1 = float(input('Dame el valor 1: '))
        valor2 = float(input('Dame el valor 2: '))
        resta = valor1 - valor2
        print(f'El resultado de la resta es: {resta}')
    elif opcion == 3:
        valor1 = float(input('Dame el valor 1: '))
        valor2 = float(input('Dame el valor 2: '))
        multi = valor1 * valor2
        print(f'El resultado de la multiplicacion es: {multi}')
    elif opcion == 4:
        valor1 = float(input('Dame el valor 1: '))
        valor2 = float(input('Dame el valor 2: '))
        div = valor1 / valor2
        print(f'El resultado de la resta es: {div}')
    elif opcion == 5:
        print('Saliendo del programa calculadora. Hasta pronto...')
        salir = True
