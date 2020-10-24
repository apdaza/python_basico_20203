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

class Tiple(Instrumento):

    def afinar(self):
        print("afinando tiple")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando tiple")
        else:
            print("tocando tiple en " + nota)

class Violin(Instrumento):

    def afinar(self):
        print("afinando violin")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando violin")
        else:
            print("tocando violin en " + nota)

class Flauta(Instrumento):

    def afinar(self):
        print("afinando flauta")

    def tocar(self, nota = None):
        if nota is None:
            print("tocando flauta")
        else:
            print("tocando flauta en " + nota)

if __name__ == "__main__":
    i = Bajo()
    i.afinar()
    i.tocar()
    i.tocar("Do")

    i = Guitarra()
    i.afinar()
    i.tocar()
    i.tocar("Do")