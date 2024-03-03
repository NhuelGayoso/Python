from teclado import Teclado
from raton import Raton
from monitor import Monitor
from orden import Orden
from computadora import Computadora

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Hyperx', 'USB')
raton2 = Raton('Hyperx', 'USB')
monitor2 = Monitor('LG', 27)
computadora2 = Computadora('Gamer',monitor2, teclado2,raton2)

computadora1 = [computadora1,computadora2]

orden1 = Orden(computadora1)
# print(orden1)

teclado3 = Teclado('Apple', 'Bluetooth')
raton3 = Raton('Apple', 'Bluetooth')
monitor3 = Monitor('Apple', 27)
computadora3 = Computadora('Apple', teclado3, raton2 , monitor1)

orden1.agregar_computadora(computadora3)
print(orden1)