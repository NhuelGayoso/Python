from raton import Raton
from teclado import Teclado
from monitor import Monitor


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self) -> str:
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''


# Codigo principal
if __name__ == '__main__':  # Para q no se ejecute desde el archivo de cada clase
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 27)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
