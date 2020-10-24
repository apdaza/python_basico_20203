from musicos import *
from random import randint

class Banda:

    def __init__(self):
        self.musicos = []

    def presentar(self):
        for m in self.musicos:
            m.presentar()

    def afinar(self):
        for m in self.musicos:
            m.afinar()

    def tocar(self):
        for m in self.musicos:
            m.tocar()

    def generar_banda(self):
        nombres = ["Juan", "Pedro", "Maria", "Miguel", "Diana", "Juana"]
        for m in range(randint(0,10)):
            self.musicos += [Musico(nombres[randint(0,len(nombres)-1)], self.generar_instrumento())]

    def generar_instrumento(self):
        opc = randint(0,5)
        if opc == 1:
            return Guitarra()
        elif opc == 2:
            return Tiple()
        elif opc == 3:
            return Flauta()
        elif opc == 4:
            return Violin()
        else:
            return Bajo()

if __name__ == "__main__":
    b = Banda()
    b.generar_banda()
    b.presentar()
    b.afinar()
    b.tocar()