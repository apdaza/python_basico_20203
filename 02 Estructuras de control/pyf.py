from random import randint

secreto = ""

while True:
    n = randint(0,9)
    if str(n) not in secreto:
        secreto += str(n)
    if len(secreto) == 3:
        break

intentos = 0

while True:
    intentos += 1
    picas = 0
    fijas = 0
    while True:
        numero = input("ingrese un numero ")
        if len(numero) == 3:
            break
    
    for i in range(3):
        for j in range(3):
            if numero[i] == secreto[j]:
                if i == j:
                    fijas += 1
                else:
                    picas += 1

    print(intentos, "picas = ", picas, "fijas = ", fijas)

    if fijas == 3:
        print("ganaste")
        break

    if intentos == 10:
        print("lo siento el numero es ", secreto)
        break

