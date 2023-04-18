class persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self__edad= edad

    def obtener_edad(self):
        return self.__edad
    
    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
    
    def presentarse(self):
        print("Hola, me llamo", self.nombre, "y tengo", self.obtener_edad(), "años")
    
objeto1 = persona("Carlos Samuel Enriquez Plascencia",21)
    
objeto1.establecer_edad(21)  
objeto1.__edad = -10 
objeto1.presentarse()  