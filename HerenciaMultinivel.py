import os
os.system('cls')

# Definir la Superclase vehiculo


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalle(self):
        print(f'Marca: {self.marca}, Modelo {self.modelo}')


# definir la subclase que hereda de vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Vehiculo.__init__()
        self.num_puertas = num_puertas

    def mostrar_detalle(self):
        super().mostrar_detalle()  # Vehiculo.mostrar_detalle()
        print(f'Numero de puertas: {self.num_puertas}')


# Definir la subclase que hereda de coche
class CocheDeportivo(Coche):
    def __init__(self, marca, modelo, num_puertas, velocidad_max):
        super().__init__(marca, modelo, num_puertas)
        self.velocidad_max = velocidad_max

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f'Velocidad maxima: {self.velocidad_max} Km/h')


# Crear una instancia de coche deportivo
mi_coche_deportivo = CocheDeportivo('Ferrari', '488', 2, 330)

# Mostrar detalles
mi_coche_deportivo.mostrar_detalle()
