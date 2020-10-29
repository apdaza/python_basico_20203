f = open("demo_escritura.txt", "w")
f.write("agregando contenido al archivo")
f.close()

f = open("demo_escritura.txt", "r")
print(f.read())
f.close()