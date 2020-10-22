def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def factorial_iterativo(numero):
    acumulador = 1
    contador = numero
    for n in range(numero):
        acumulador *= contador
        contador -= 1
    return acumulador



print(factorial(3))
print(factorial_iterativo(3))
