def generar_matriz(archivo):
    f = open(archivo)
    lineas = f.readlines()
    f.close()

    lineas = [x.strip("\n") for x in lineas]
    matriz = [x.split(",") for x in lineas]

    return matriz

def escribir_titulos(objeto_archivo,lista):
    cad = ""
    for e in lista:
        cad += e + ","
    cad += "resultado\n"
    objeto_archivo.write(cad)

def escribir_resultados(archivo, matriz):
    f = open(archivo, "w")
    escribir_titulos(f,matriz[0])
    for r in matriz[1:]:
        acumulador = 0
        for d in r:
            f.write(d+",")
            acumulador += int(d)
        f.write(str(acumulador)+"\n")
    f.close()

matriz = generar_matriz("datos.csv")
escribir_resultados("resultados.csv", matriz)

 


