class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')


class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def trabajar(self):
        print(f'{self.nombre} esta trabajando como {self.puesto}')


persona1 = Persona('Ana', 30)
persona1.presentarse()

empleado1 = Empleado('Carlos', 45, 'Ingeniero')
empleado1.presentarse()
empleado1.trabajar()
