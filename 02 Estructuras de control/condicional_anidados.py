x = int(input("Ingrese un valor entero: "))
print("Usted ingreso el: " + str(x))

if x % 4 == 0:
    x /= 4
else:
    if x % 2 == 0:
        x /= 2
    else:
        if x % 3 == 0:
            x /= 3
        else:
            x += 1

 


print("Ahora el valor es: " + str(x))
