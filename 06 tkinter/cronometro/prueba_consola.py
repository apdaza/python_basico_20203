from cronometro import Cronometro

c = Cronometro()
for i in range(1000):
    c.avanzar()
    print(c.get_tiempo())