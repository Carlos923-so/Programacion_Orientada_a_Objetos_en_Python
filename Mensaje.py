class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
    
    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print("Acelerando... Velocidad actual:", self.velocidad)
        
    def frenar(self, cantidad):
        self.velocidad -= cantidad
        print("Frenando... Velocidad actual:", self.velocidad)
        
mi_coche = Coche("Toyota", "Corolla", "Rojo")
mi_coche.acelerar(50) 
mi_coche.frenar(20) 
