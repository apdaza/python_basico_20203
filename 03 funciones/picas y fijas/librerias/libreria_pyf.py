from random import randint

def generar_secreto():
    secreto = ""
    while True:
        n = randint(0,9)
        if str(n) not in secreto:
            secreto += str(n)
        if len(secreto) == 3:
            break
    return secreto

def capturar_numero():
    while True:
        numero = input("ingrese un numero ")
        if len(numero) == 3:
            break
    return numero

def comparar(secreto, numero):
    picas = 0
    fijas = 0
    for i in range(3):
        for j in range(3):
            if numero[i] == secreto[j]:
                if i == j:
                    fijas += 1
                else:
                    picas += 1
    return picas, fijas