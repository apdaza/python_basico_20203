import tkinter as tk

def actuador1():
    print("Boton 1")

def actuador2():
    print("Boton 2")

def actuador3():
    print("Boton 3")

ventana = tk.Tk()
ventana.geometry("300x100")
boton1 = tk.Button(ventana, text="Boton 1", command=actuador1)
boton1.pack()
boton2 = tk.Button(ventana, text="Boton 2", command=actuador2)
boton2.pack()
boton3 = tk.Button(ventana, text="Boton 3", command=actuador3)
boton3.pack()

ventana.mainloop()
