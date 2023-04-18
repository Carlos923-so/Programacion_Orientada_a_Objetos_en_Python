class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        
    def apagar(self):
        self.encendido = False
mi_coche = Coche("Ford", "Mustang", "rojo")
print(mi_coche.encendido)  # False
mi_coche.encender()
print(mi_coche.encendido)  # True
mi_coche.apagar()
print(mi_coche.encendido)  # False