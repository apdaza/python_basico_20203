import os

if os.path.exists("demo_crear.txt"):
    print("el archivo existe")
else:
    f = open("demo_crear.txt", "x")