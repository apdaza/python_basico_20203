from random import shuffle

class Carta:

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def informar_valor(self):
        if self.valor in ["J", "Q", "K"]:
            return 10
        elif self.valor == "A":
            return 1
        else:
            return int(self.valor)

    def mostrar_carta(self):
        print(self.valor, self.pinta)

class Mazo:

    def __init__(self, jugador = False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [Carta(v, p) for v in ["A", "J", "Q", "K"] + [str(x) for x in range(2, 11)]  for p in ["Treboles", "Picas", "Diamantes", "Corazones"]]
            shuffle(self.cartas)

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def entregar_carta(self):
        if self.cartas != []:
            carta = self.cartas[0]
            self.cartas = self.cartas[1:]
        else:
            carta = None # evaluar entregar un comodin
        return carta

    def informar_valor(self):
        valor = 0
        for c in self.cartas:
            valor += c.informar_valor()
        tiene_as = False
        for c in self.cartas:
            if c.valor == "A":
                tiene_as = True
                break
        
        if tiene_as and valor <= 11:
            valor += 10 

        return valor

    def mostrar_cartas(self, todas=False):
        if todas:
            for c in self.cartas:
                c.mostrar_carta()
        else:
            for c in self.cartas[1:]:
                c.mostrar_carta()

if __name__ == "__main__":
    m = Mazo()
    m.agregar_carta(Carta("A", "Treboles"))
    m.agregar_carta(Carta("5", "Diamantes"))
    m.agregar_carta(Carta("Q", "Picas"))
    print(m.informar_valor())
    m.mostrar_cartas(True)
    carta = m.entregar_carta()
    carta.mostrar_carta()
    print(m.informar_valor())