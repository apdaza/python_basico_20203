"""
Ejemplos de nombres de variables validas
y no validas
"""
_mi_variable_ = "un valor"
MiVariable = "un valor"
mi_variable_0 = "un valor"

_mivariable2_ = "un valor"

Mivariable = 'un "hola" valor'

print(MiVariable == Mivariable)
print(Mivariable)

x, y, z = 32, 21, 5

print(x, y, z)
print(x)


x = y = z = 25

print(x, y, z)
print(x)

x = "genial"


def mi_funcion():
    global x
    x = "facil"
    print("python es " + x)
    y = 5
    print(y)

mi_funcion()
print("python es " + x)          
print(type(y))
print(type(x))
