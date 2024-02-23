snacks = [
    {'id': 0, 'nombre': 'Papas', 'precio': 30},
    {'id': 1, 'nombre': 'Refresco', 'precio': 50},
    {'id': 2, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de producto (vacia)
productos = []

print('*** Maquina de Snack ***')
print('Snacks Disponibles: ')
for snack in snacks:
    print(f'\tId: {snack['id']}'
          f'-> Producto: {snack['nombre']}'
          f' - Precio: {snack['precio']}')


def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print(f'''Menu:
        1. Comprar Snack
        2. Mostrar Ticket
        3. Salir''')
        opcion = int(input('Escoge una opcion: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            print('Regresa pronto!')
            salir = True
        else:
            print('Opcion invalida, selecciona otra opcion')


def comprar_producto(snack, productos):
    id_snack = int(input('Que snack quieres (id)?: '))
    productos.append(snacks[id_snack])
    print(f'Ok. snack agregado: {snacks[id_snack]}')


def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de venta ***'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto['nombre']} - ${producto['precio']}'
        total += producto['precio']
    ticket += f'\n\tTotal -> ${total}'
    print(ticket)


# Llamamos o invocamos la funcion maquina_snacks
maquina_snacks(snacks, productos)
