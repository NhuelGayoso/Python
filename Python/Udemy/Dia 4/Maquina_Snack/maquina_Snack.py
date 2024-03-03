from snacks import Snacks
from snack import Snack

# Lista de producto (vacia)
productos = []

print('*** Maquina de Snack ***')
print('Snacks Disponibles: ')
snacks = Snacks()
print(snacks)


def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print(f'''Menu:
        1. Comprar Snack
        2. Mostrar Ticket
        3. Agregar Snack
        4. Salir''')
        opcion = int(input('Escoge una opcion: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            agregar_snack(snacks)
        elif opcion == 4:
            print('Regresa pronto!')
            salir = True
        else:
            print('Opcion invalida, selecciona otra opcion')


def comprar_producto(snack, productos):
    id_snack = int(input('Que snack quieres (id)?: '))
    # productos.append(snacks[id_snack])
    # print(f'Ok. snack agregado: {snacks[id_snack]}')

    # Reccorrer la lista de snacks
    snack_encotrado = None
    for snack in snacks.lista_snacks:
        if id_snack == snack.id:
            snack_encotrado = snack
            break
    if snack_encotrado is not None:
        productos.append(snack_encotrado)
        print(f'Pk, snack agregado: {snack_encotrado}')
    else:
        print(f'El id del snack es incorrecto: {id_snack}')


def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de venta ***'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto.nombre} - ${producto.precio}'
        total += producto.precio
    ticket += f'\n\tTotal -> ${total}'
    print(ticket)


def agregar_snack(snacks):
    nombre = input('Dame el nomvre del nuevo snack ')
    precio = int(input('Dame el precio del snack '))
    nuevo_snack = Snack(nombre, precio)
    snacks.agregar_snack(nuevo_snack)
    print(f'Tu snack {nuevo_snack} se agrego correctamente')
    print(snacks)


# Llamamos o invocamos la funcion maquina_snacks
maquina_snacks(snacks, productos)
