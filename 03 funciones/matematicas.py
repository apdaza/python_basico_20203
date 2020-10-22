def suma(valor1, valor2):
    return valor1 + valor2

def resta(valor1, valor2):
    return valor1 - valor2

def multiplicacion(valor1, valor2):
    return valor1 * valor2

def division(valor1, valor2 = 1):
    return valor1 // valor2

def incrementar(valor):
    global valor1
    valor1 += valor
    print(valor1)


valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

resultado = suma(valor1, valor2)
print(resultado)

resultado = resta(valor1, valor2)
print(resultado)

resultado = multiplicacion(valor1, valor2)
print(resultado)

resultado = division(valor1)
print(resultado)

