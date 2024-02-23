# Clase de Contacto
class Contacto:
    # Metodo
    def inicializar_contacto(self,
                             nombre, apellido,
                             celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def mostrar_contacto(self):
        print(f'''
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Celular: {self.celular}
            Email: {self.email}
        ''')
        print(f'Dir Mem self: {id(self)}')
        print(f'Dir Mem self Hex: {hex(id(self))}')


# Codigo Principal
print('*** Clases y Objetos en Python')
# Crear un primer objeto
contacto1 = Contacto()
contacto1.inicializar_contacto('layla', 'Acosta', '55667788', 'layla@mail.com')

contacto1.mostrar_contacto()
print(f'Direccion de memoria: {id(contacto1)}')
print(f'Direccion de memoria Hex: {hex(id(contacto1))}')
contacto2 = Contacto()
contacto2.inicializar_contacto(
    'Carlos', 'Perez', '55667788', 'carlos@mail.com')

contacto2.mostrar_contacto()
print(f'Direccion de memoria: {id(contacto2)}')
print(f'Direccion de memoria Hex: {hex(id(contacto2))}')