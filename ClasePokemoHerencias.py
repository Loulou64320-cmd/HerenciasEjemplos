import os
os.system('cls')


class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre


class PokemonTipo(Pokemon):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def describir(self):
        print(f'¡Hola! soy {self.nombre} un pokemon de tipo {self.tipo}')


class PokemonEvolucion(PokemonTipo):
    def __init__(self, nombre, tipo, evolucion):
        super().__init__(nombre, tipo)
        self.evolucion = evolucion

    def describir(self):
        super().describir()
        print(f'Evoluciono en {self.evolucion}\n')


pikachu = PokemonEvolucion('Pikachu', 'Electrico', 'Raichu')
pikachu.describir()

charmander = PokemonEvolucion('Charmander', 'Fuego', 'Charmeleon')
charmander.describir()
