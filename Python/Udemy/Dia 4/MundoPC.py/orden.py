class Orden:
    contador_orden = 0

    def __init__(self, computadora) -> None:
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        # Recibimos la lista objeto computadora
        self.computadora = computadora

    def agregar_computadora(self,computadora):
        self.computadora.append(computadora)
    
    def __str__(self) -> str:
        computadora_str = ''
        for computadora in self.computadora:
            computadora_str += '\n' + computadora.__str__()
        return f'''Orden: {self.id_orden}
        Computadora:
            {computadora_str}'''
