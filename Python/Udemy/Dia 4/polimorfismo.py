# Clase padre
class Animal:
    def hacer_sonido(self):
        print('Hago un sonido...')

# Clase hija


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')


class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo Maullar')


print('*** Ejemplo Polimorfismo***')
print('Clase Padre Animal')
animal1 = Animal()
animal1.hacer_sonido()

print('\nClase hija Perro')
animal2 = Perro()
animal2.hacer_sonido()
print('\nClase hija Gato')
animal3 = Gato()
animal3.hacer_sonido()