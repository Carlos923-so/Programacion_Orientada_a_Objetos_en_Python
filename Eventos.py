from tkinter import * #importar libreria tkinter
from tkinter import ttk
class Conversor:
    def __init__(self, raiz):
        #init sirve como constructor de la clase(), self que hace referencia a los elementos de la misma clase.
        raiz.title("Prueba de eventos")
        self.pies = StringVar()
        self.metros = StringVar()
        
        mainFrame=ttk.Frame(raiz) #Widgets transparentes #Instancia de raiz
        mainFrame.grid(column=0, row=0)
        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid()
        piesEntry.grid(column=1,row=0)       
        ttk.Label(mainFrame, text="Numero").grid(column=2, row=0) #Objeto
        ttk.Label(mainFrame, text="El numero ingresado es").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        
        ttk.Button(mainFrame, text="Ver", command=self.calcular).grid(column=2, row=2)
        raiz.bind("<Return>", self.calcular)   #Buscar tablas de estandares de las letras.
        
    def calcular(self, *args): #Agregar en evento calcular el args arreglo de parametros
        print("Boton presionado: ")
        piesUsuario=self.pies.get() #Siempre devuelve una cadena
        print("Numero ingresado: ", piesUsuario)
        print("Metros:",piesUsuario)
        self.metros.set(piesUsuario)
raiz= Tk()
Conversor(raiz)
raiz.mainloop()
