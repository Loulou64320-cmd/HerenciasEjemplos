import os
os.system('cls')


class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def animalito(self):
        print(f'Me llamo {self.nombre} y soy un(a) {self.especie}')


class Carnivoro:
    def __init__(self, carnivoro):
        self.carnivoro = carnivoro

    def soy_carnivoro(self):
        print(f'Soy {self.carnivoro} y como carne')


class AnimalCarnivoro(Animal, Carnivoro):
    def __init__(self, nombre, especie, carnivoro):
        Animal.__init__(self, nombre, especie)
        Carnivoro.__init__(self, carnivoro)


leon = AnimalCarnivoro('alex', 'leon', 'carnivoro')

leon.animalito()
leon.soy_carnivoro()
