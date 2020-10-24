class MiClase:
    def __init__(self, valor):
        self.x = valor

mi_objeto = MiClase(5)
mi_segundo_objeto = MiClase(5)

print(mi_objeto == mi_segundo_objeto)

print(type(mi_objeto) == type(mi_segundo_objeto))