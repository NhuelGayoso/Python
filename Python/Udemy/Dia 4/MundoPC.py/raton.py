from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    # Constructor
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        self.marca = marca
        super().__init__(marca, tipo_entrada)

    def __str__(self) -> str:
        return (f'Id: {self.id_raton}, Marca: {self.marca}, '
                f'Tipo entrada: {self.tipo_entrada}')


# Codigo Principal
if __name__ == '__main__':
    raton1 = Raton('HP', 'usb')
    print(raton1)
    raton2 = Raton('Hyperx', 'Inalambrico')
    print(raton2)
