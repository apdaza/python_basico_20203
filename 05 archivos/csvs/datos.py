lineas = open("datos.csv").readlines()

lineas = [x.strip("\n") for x in lineas]

matriz = [x.split(",") for x in lineas]

for l in matriz:
    for e in l:
        print(e, end="\t")
    print()