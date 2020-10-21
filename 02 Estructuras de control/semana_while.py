semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]


while True:
    dia = int(input("Ingrese un valor para el dia de la semana: "))
    if dia >= 1 and dia <= 7:
        break

print(semana[dia - 1])