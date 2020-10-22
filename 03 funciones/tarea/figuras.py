from math import sqrt, pi

def distancia_ejes(v1, v2):
    return abs(v1 - v2)

def distancia(punto1, punto2):
    return sqrt(((punto1[0]-punto2[0])**2) + ((punto1[1]-punto2[1])**2))

def capturar_punto():
    x = int(input("ingrese le valor de x: "))
    y = int(input("ingrese le valor de y: "))
    return x, y

def area_cuadrado(punto1, punto2):
    area = distancia_ejes(punto1[0], punto2[0]) * distancia_ejes(punto1[1], punto2[1])
    return area

def perimetro_cuadrado(punto1, punto2):
    perimetro = (2 * distancia_ejes(punto1[0], punto2[0])) + (2 * distancia_ejes(punto1[1], punto2[1]))
    return perimetro

def area_circulo(punto1, punto2):
    area = pi * distancia(punto1, punto2)**2
    return area

def perimetro_circulo(punto1, punto2):
    perimetro = 2 * pi * distancia(punto1, punto2)
    return perimetro

punto1 = capturar_punto()
punto2 = capturar_punto()

print("area del cuadrado: ", area_cuadrado(punto1, punto2))
print("perimetro del cuadrado: ", perimetro_cuadrado(punto1, punto2))

print("area del circulo: ", area_circulo(punto1, punto2))
print("perimetro del circulo: ", perimetro_circulo(punto1, punto2))