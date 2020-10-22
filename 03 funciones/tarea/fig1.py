#Vivian
#Erick 
#Jeisson Alfonso
#julio duran

from math import fabs, pi,sqrt #Paquetes
print("Area y Perimetro de un circulo y un Cuadrado")
y1=int(input('Ingrese el valor de y1: '))
x1=int(input('Ingrese el valor de x1: '))
y2=int(input('Ingrese el valor de y2: '))
x2=int(input('Ingrese el valor de x2: '))
#cuadrado
#calculo de las distancias del circulo:
def circ(x1,x2,y1,y2):
  r=sqrt((x2-x1)**2+(y2-y1)**2) #radio del Circulo
  A=pi*r**2 #area
  p=2*pi*r # perimetro del circulo
  return print('Radio del circulo= ',r, 'Perimetro del circulo= ',p, 'Area del circulo= ',A) 

#cálculo de las distancias del rectangulo:
def cua(x1,x2,y1,y2):
  if x2!=x1 and y2!=y1:
   b=fabs(x1-x2) #base
   a=fabs(y1-y2) #altura
   A=a*b #area
   P=2*a+2*b #perimetro
   print('Area del cuadrado=', A, 'Perimetro del cuadrado=', P)
  else:
    print ('no hay cuadrado')
  #return print('Area del cuadrado=', A, 'Perimetro del cuadrado=', P)

cua(x1,x2,y1,y2)
circ(x1,x2,y1,y2)