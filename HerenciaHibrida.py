import os
os.system('cls')


class SerVivo():
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f'Mi nombre es {self.nombre}')


class Animal(SerVivo):
    def __init__(self, nombre, especie):
        super().__init__(nombre)
        self.especie = especie

    def mostrar_especie(self):
        print(f'soy un(a) {self.especie}')


class Planta(SerVivo):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def mostrar_tipo(self):
        print(f'soy un(a) {self.tipo}')


class Carnivoro():
    def __init__(self):
        self.dieta = dieta

    def soy_carnivoro(self):
        print(f'soy carnivoro y como {self.dieta}')


class AnimalCarnivoro(Animal, Carnivoro):
    def __init__(self, nombre, especie):
        Animal.__init__(self, nombre, especie)
        Carnivoro.__init__(self)


class Hervivoro():
    def __init__(self):
        self.dieta = dieta


class AnimalHervivoro(Animal, Hervivoro):
    def __init__(self, nombre, especie):
        Animal.__init__(self, nombre, especie)
        Hervivoro.__init__(self)


class PlantaCarnivora(Planta, Carnivoro):
    def __init__(self, nombre, tipo):
        Planta.__init__(self, nombre, tipo)
        Carnivoro.__init__(self)


animal = Animal('alex', 'leon')
animal.mostrar_nombre()
animal.mostrar_especie()
animal.soy_carnivoro()

planta = Planta('grud', 'arbol')
planta.mostrar_nombre()
planta.mostrar_tipo()
