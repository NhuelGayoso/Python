from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0
    
    # Constructor
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        self.marca = marca
        super().__init__(marca, tipo_entrada)    
    
    def __str__(self):
        return (f'Id: {self.id_teclado}, Marca: {self.marca} '
                f'Tipo entrada: {self.tipo_entrada}')

# Codigo principal
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'usb')
    print(teclado1)
    teclado2 = Teclado('Hyperx', 'inalambrico')
    print(teclado2)