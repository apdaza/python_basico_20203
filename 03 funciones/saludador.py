def saludar(nombre):
    print("hola " + nombre)

def saludar_invitados(invitados):
    for n in invitados:
        saludar(n)


saludar_invitados(["Alejandro", "Maria", "Juan"])