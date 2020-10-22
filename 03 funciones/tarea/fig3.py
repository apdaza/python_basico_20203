# Programa de Figuras Geometricas
# Integrantes
# Andres Cardenas Contreras
# Juan Sebastian Parraga
# Figuras geometricas
from math import pi, sqrt

x1 = int(input("Ingrese la coordenada x1: "))
y1 = int(input("Ingrese la coordenada y1: "))

               
x2 = int(input("Ingrese la coordenada x2: "))
y2 = int(input("Ingrese la coordenada y2: "))




# Circulo
radio = sqrt((x2-x1)**2 + (y2-y1)**2)

def area_circulo(radio):
    return pi*radio**2

def perimetro_circulo(radio):
    return 2*pi*radio

# Rectangulo

altura = abs(y2-y1)
base = abs(x2-x1)

def area_rectan(base,altura):
    return base*altura

def perimetro_rectan(base,altura):
    return 2*base+2*altura

print("Circulo")
area_cir = area_circulo(radio)
print("area circulo: " +str(area_cir))


perimetro_cir = perimetro_circulo(radio)
print("perimetro circulo: " +str(perimetro_cir))


print("Rectangulo")
area_rect = area_rectan(base,altura)
print("area rectangulo: " +str(area_rect))


perimetro_rect = perimetro_rectan(base,altura)
print("perimetro rectangulo: " +str(perimetro_rect))
  