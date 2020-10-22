from librerias.libreria_pyf import *

intentos = 0
secreto = generar_secreto()

while True:
    intentos += 1
    numero = capturar_numero()    
    picas, fijas = comparar(secreto, numero)
    print(intentos, "picas = ", picas, "fijas = ", fijas)
    if fijas == 3:
        print("ganaste")
        break
    if intentos == 5:
        print("lo siento el numero es ", secreto)
        break

