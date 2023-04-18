class Habitacion:
    def __init__(self, nombre, ancho, largo):
        self.nombre = nombre
        self.ancho = ancho
        self.largo = largo
        
class Casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        
mi_casa = Casa("Mi Casa")
habitacion1 = Habitacion("Sala", 4, 5)
habitacion2 = Habitacion("Dormitorio", 3, 4)

mi_casa.agregar_habitacion(habitacion1)
mi_casa.agregar_habitacion(habitacion2)

print("Mi casa tiene las siguientes habitaciones:")
for habitacion in mi_casa.habitaciones:
    print(f"{habitacion.nombre}: {habitacion.ancho}m x {habitacion.largo}m")
