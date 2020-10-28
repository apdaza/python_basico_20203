from cartas import *

mazo = Mazo()
mazo.mostrar_cartas(True)


jugador1 = Mazo()
jugador1.agregar_carta(mazo.entregar_carta())
jugador1.agregar_carta(mazo.entregar_carta())

jugador2 = Mazo()
jugador2.agregar_carta(mazo.entregar_carta())
jugador2.agregar_carta(mazo.entregar_carta())


if jugador1.informar_valor() > jugador2.informar_valor():
    print("gana jugador 1")
elif jugador1.informar_valor() < jugador2.informar_valor():
    print("gana jugador 2")
else:
    print("empate")
