import os

if os.path.exists("demo_crear.txt"):
    os.remove("demo_crear.txt")
else:
    print("No existe el archivo demo_crear.txt")