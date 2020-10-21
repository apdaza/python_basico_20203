x = int(input("Ingrese un valor entero: "))
print("Usted ingreso el: " + str(x))

if x % 4 == 0:
    x = x / 4

if x % 2 == 0:
    x = x / 2

if x % 3 == 0:
    x = x / 3

 


print("Ahora el valor es: " + str(x))
