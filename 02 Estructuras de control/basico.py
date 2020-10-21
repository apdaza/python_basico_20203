x = int(input("Ingrese un valor entero: "))
print("Usted ingreso el: " + str(x))

if x % 2 == 0:
    x = x / 2
elif x % 3 == 0:
    x = x / 3
elif x % 4 == 0:
    x = x / 4 
else:
    x = x + 1

print("Ahora el valor es: " + str(x))
