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
        print(f'¡Hola! Soy {self.nombre}, un Pokémon de tipo {self.tipo}.')


class PokemonEvolucion(PokemonTipo):
    def __init__(self, nombre, tipo, evolucion):
        super().__init__(nombre, tipo)
        self.evolucion = evolucion

    def describir(self):
        super().describir()
        print(f'Evoluciono en {self.evolucion}.\n')

# Clase derivada con habilidades


class PokemonHabilidad(PokemonEvolucion):
    def __init__(self, nombre, tipo, evolucion, habilidad):
        super().__init__(nombre, tipo, evolucion)
        self.habilidad = habilidad

    def describir(self):
        super().describir()
        print(f'Tengo la habilidad {self.habilidad}.')

# Clase derivada con estadísticas de batalla


class PokemonBatalla(PokemonHabilidad):
    def __init__(self, nombre, tipo, evolucion, habilidad, ataque, defensa):
        super().__init__(nombre, tipo, evolucion, habilidad)
        self.ataque = ataque
        self.defensa = defensa

    def describir(self):
        super().describir()
        print(
            f'Mis estadísticas de batalla son - Ataque: {self.ataque}, Defensa: {self.defensa}.\n')


# Ejemplos
bulbasaur = PokemonBatalla(
    'Bulbasaur', 'Planta/Veneno', 'Ivysaur', 'Clorofila', 49, 49)
bulbasaur.describir()

charmander = PokemonBatalla('Charmander', 'Fuego',
                            'Charmeleon', 'Mar Llamas', 52, 43)
charmander.describir()

squirtle = PokemonBatalla('Squirtle', 'Agua', 'Wartortle', 'Torrente', 48, 65)
squirtle.describir()
