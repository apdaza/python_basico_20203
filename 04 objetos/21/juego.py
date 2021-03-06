from cartas import *

class Juego:

    def __init__(self):
        self.mazo = Mazo()
        self.jugador1 = Mazo(True)
        self.jugador2 = Mazo(True)

    def iniciar_partida(self):
        for i in range(2):
            self.jugador1.agregar_carta(self.mazo.entregar_carta())
            self.jugador2.agregar_carta(self.mazo.entregar_carta())

    def mostrar_juego(self, finalizado = False):
        print("Cartas jugador 1")
        self.jugador1.mostrar_cartas(finalizado)
        print("Cartas jugador 2")
        self.jugador2.mostrar_cartas(finalizado)
        if finalizado:
            valor1 = self.jugador1.informar_valor()
            valor2 = self.jugador2.informar_valor()
            print(valor1, valor2)
            if valor1 > valor2 and valor1 <= 21:
                print("Gana jugador 1") 
            elif valor1 < valor2 and valor2 <= 21:
                print("Gana jugador 2")
            elif valor1 > valor2 and valor1 > 21:
                print("Gana jugador 2") 
            elif valor1 < valor2 and valor2 > 21:
                print("Gana jugador 1")
            else:
                print("Empate")


    def jugar(self):
        jugando = True
        self.iniciar_partida()
        while jugando:
            self.mostrar_juego()
            print("*" * 10)
            if self.jugador1.informar_valor() < 18:
                self.jugador1.agregar_carta(self.mazo.entregar_carta())
            if self.jugador2.informar_valor() < 18:
                self.jugador2.agregar_carta(self.mazo.entregar_carta())
            if self.jugador1.informar_valor() > 21:
                jugando = False
                break 
            if self.jugador2.informar_valor() > 21:
                jugando = False
                break
            if self.jugador1.informar_valor() >= 18 and self.jugador2.informar_valor() >= 18:
                jugando = False
            if self.jugador1.cartas[-1].informar_valor() == 0 or self.jugador2.cartas[-1].informar_valor() == 0: 
                jugando = False
                break

        self.mostrar_juego(True)
            


