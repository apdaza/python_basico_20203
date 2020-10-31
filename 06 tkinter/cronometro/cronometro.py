from unidades import UnidadDeTiempo

class Cronometro:
    def __init__(self):
        self.hora = UnidadDeTiempo(23)
        self.minuto = UnidadDeTiempo()
        self.segundo = UnidadDeTiempo()
        self.parado = True

    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor == 0:
            self.minuto.avanzar()
            if self.minuto.valor == 0:
                self.hora.avanzar()

    def borrar(self):
        self.hora.borrar()
        self.minuto.borrar()
        self.segundo.borrar()

    def get_tiempo(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hora.valor, self.minuto.valor, self.segundo.valor)

    def cambiar_estado(self):
        self.parado = not self.parado