# Reto de calculadora con funciones
# 1. Solicitar el menu en una funcion
# 2. Solicitar los valores de los operadores en una funcion
# 3. La operacion a ejecutar va en otra funcion por separado
print('*** Calculadora en Python con Funciones ***')

# ''' Definimos la funcion de mostrar_menu'''
print('*** Calculadora en Pyhton ***')


def mostrar_menu():
    print('''
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir
    ''')
    opcion = int(input('Escoge una opcion: '))
    return opcion


# ''' Definimos la funcion para solicitar los valores '''
def pedir_valores():
    num1 = float(input('Ingrse el primer valor: '))
    num2 = float(input('Ingrse el segundo valor: '))
    return num1, num2


# ''' Definimos la funcion para ejecutar la operacion solicitante '''
def ejecutar_operacion(opcion, salir):
    # solicitamos en primer lugar los valores de los operando
    if opcion > 0 and opcion < 5:
        operando1, operando2 = pedir_valores()
        resultado = 0
    if opcion == 1:
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado}')
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'El resultado de la division es: {resultado}')
    elif opcion == 5:
        print('Saliendo del programa calculadora. Hasta pronto')
        salir = True
        
    return salir

# Codigo principal
salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)
