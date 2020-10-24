class Calculadora:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0
        self.resultado = 0

    def sumar(self):
        self.resultado = self.v1 + self.v2

    def restar(self):
        self.resultado = self.v1 - self.v2

    def multiplicar(self):
        self.resultado = self.v1 * self.v2

    def dividir(self):
        self.resultado = self.v1 // self.v2

cal = Calculadora()

cal.v1 = 5
cal.v2 = 3

cal.restar()
print(cal.resultado)