# Clase padre
class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

# Clase hija


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    def dormir(self):
        print('Duermo 15 horas al dia')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puede maullar')
    def dormir(self):
        print('Duerma en la tarde')

print('*** Ejemplo Herencia en Python')
print('Clase padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
# animal1.hacer_sonido() manda error, metodo de la clase hija

print('\nClase hija, soy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()  # Sobreescrito en la clase hija
perro1.hacer_sonido()
