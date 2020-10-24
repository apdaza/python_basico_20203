from random import randint

class Animal:

    def informar_tipo(self):
        print(type(self))

    def comunicar(self):
        pass

class Gato(Animal):

    def comunicar(self):
        print("miau")

class Perro(Animal):

    def comunicar(self):
        print("guau")

class Gusano(Animal):
    
    def comunicar(self):
        print("sssss")

class Perico(Animal):

    def comunicar(self):
        print("rua")

class Paloma(Animal):

    def comunicar(self):
        print("cucurucucu")


class Tienda:
    def __init__(self):
        self.animales = []

    def generar_animal(self):
        opc = randint(0, 4)
        if opc == 0:
            return Gato()
        elif opc == 1:
            return Perro()
        elif opc == 2:
            return Perico()
        elif opc == 3:
            return Paloma()
        else:
            return Gusano()

    def generar_animales(self, cant):
        for i in range(cant):
            self.animales += [self.generar_animal()]

    def mostrar_animales(self):
        for a in self.animales:
            a.informar_tipo()
            a.comunicar()



