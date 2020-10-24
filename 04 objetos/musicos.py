from instrumentos import *

class Musico:
    
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def presentar(self):
        print("yo soy " + self.nombre)
        print("y toco " + str(type(self.instrumento)))

if __name__ == "__main__":
    m = Musico("Juan", Guitarra())
    m.presentar()
