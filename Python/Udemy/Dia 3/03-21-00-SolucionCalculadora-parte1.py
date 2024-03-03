# Reto Calculadora con funciones
print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta 
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opcion: '))
    return opcion

def pedir_valores():
    op1 = float(input('Dame el valor 1: '))
    op2 = float(input('Dame el valor 2: '))
    return op1, op2

def ejecutar_operacion(opcion, salir):
    pass

# Codigo principal
salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)