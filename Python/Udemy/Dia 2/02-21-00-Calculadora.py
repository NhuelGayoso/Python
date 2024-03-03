# Reto de Calculadora
print('*** Calculadora en Python ***')
operando1 = operando2 = resultado = 0  # Definimos las variables
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opcion: '))
    # Solicitamos los valores
    #if opcion >= 1 and opcion <=4:
    if 1 <= opcion <= 4:
        operando1 = float(input('Dame el valor 1: '))
        operando2 = float(input('Dame el valor 2: '))
    # Revisamos el tipo de operacion a realizar
    if opcion == 1:  # Suma
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:  # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:  # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado:.2f}\n')
    elif opcion == 4:  # Division
        resultado = operando1 / operando2
        print(f'El resultado de la division es: {resultado:.2f}\n')
    elif opcion == 5:
        salir = True
        print('Saliendo del programa Calculadora. Hasta pronto!')
    else:
        print('Opcion invalida, selecciona otra opcion...\n')