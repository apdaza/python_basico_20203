class Instrumento:

    def afinar(self):
        pass

    def tocar(self, nota = None):
        pass

class Guitarra(Instrumento):

    def afinar(self):
        print("afinando guitarra")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando guitarra")
        else:
            print("tocando guitarra en " + nota)

class Bajo(Instrumento):

    def afinar(self):
        print("afinando bajo")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando bajo")
        else:
            print("tocando bajo en " + nota)

if __name__ == "__main__":
    i = Bajo()
    i.afinar()
    i.tocar()
    i.tocar("Do")

    i = Guitarra()
    i.afinar()
    i.tocar()
    i.tocar("Do")