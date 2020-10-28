from figuras import *

opcion = input("ingrese el tipo de figura: \n 1. cuadrado \n 2. circulo \n 3. triangulo \n 4. rectangulo ")

if opcion == "1":
    f = Cuadrado(Punto(5,10), Punto(10,15))
elif opcion == "2":
    f = Circulo(Punto(5,10), Punto(10,15))
elif opcion == "3":
    f = Triangulo(Punto(5,10), Punto(10,15))
else:
    f = Rectangulo(Punto(5,10), Punto(10,15))

f.calcular_area()
f.calcular_perimetro()
f.informar_propiedades()
