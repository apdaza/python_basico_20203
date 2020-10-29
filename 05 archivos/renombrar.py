import os

lista = os.listdir("archivos_renombrables")

for e in lista:
    print(e)
    if os.path.exists("archivos_renombrables/"+ str(e)):
        os.rename("archivos_renombrables/" + str(e), "archivos_renombrables/renombrado_" + str(e))
    else:
        print("no puedo renombrar archivo")

