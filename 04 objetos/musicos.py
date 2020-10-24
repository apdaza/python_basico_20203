from instrumentos import *

class Musico:
    
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def presentar(self):
        print("yo soy " + self.nombre)
        print("y toco " + str(type(self.instrumento)))

    def afinar(self):
        self.instrumento.afinar()
        self.instrumento.tocar("Do")

    def tocar(self):
        self.instrumento.tocar()

if __name__ == "__main__":
    m = Musico("Juan", Guitarra())
    m.presentar()
    m.afinar()
    m.tocar()
