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
    pass

class Perico(Animal):

    def comunicar(self):
        print("rua")


def generar_animal():
    opc = randint(0, 4)
    if opc == 0:
        return Gato()
    elif opc == 1:
        return Perro()
    elif opc == 2:
        return Perico()
    else:
        return Gusano()



a = generar_animal()
a.comunicar()
a.informar_tipo()