class Monitor:
    contador_monitor = 0

    def __init__(self,marca, tamanio):
        Monitor.contador_monitor += 1
        self.id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamanio = tamanio
        

    def __str__(self) -> str:
        return (f'Id: {self.id_monitor}, Marca: {self.marca} '
                f'Tamaño: {self.tamanio}')

# Codigo Principal
if __name__ == '__main__':
    monitor1 = Monitor('LG','20 pulgadas')
    print(monitor1)