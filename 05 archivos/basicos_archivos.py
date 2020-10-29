"""
open(nombre_archivo, modo)

open(nombre_archivo, "r") -> solo lectura -> error si no existe el archivo
open(nombre_archivo, "a") -> agregar contenido al archivo -> crea el archivo si no existe
open(nombre_archivo, "w") -> modo de escritura en el archivo -> crea el archivo si no existe
open(nombre_archivo, "x") -> crear el archivo -> si el archivo esxiste me generar error

"""
f = open("demo.txt")
print(f.read())

f = open("C:\\Users\Alejandro\Documents\demo_c.txt")
print(f.read())

f = open("archivos/demo_archivos.txt")
print(f.read())

f = open("../demo_archivos.txt", "r")
print(f.read())

f = open("demo.txt")
print(f.read(10))

f = open("demo.txt")
print(f.readline())