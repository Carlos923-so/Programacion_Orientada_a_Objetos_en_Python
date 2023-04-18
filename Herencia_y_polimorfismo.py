class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def trabajar(self):
        pass

class Programador(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def trabajar(self):
        print("Operar paciente")

class Doctor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def trabajar(self):
        print("Programar")
        
programador = Programador("Carlos Samuel Enriquez Plascencia")
doctor = Doctor("Nosborn")

programador.trabajar()
doctor.trabajar()
