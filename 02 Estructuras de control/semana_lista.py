dia = int(input("Ingrese un valor: "))

semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

if dia < 1 or dia > 7:
    print("valor no valido")
else:
    print(semana[dia - 1])