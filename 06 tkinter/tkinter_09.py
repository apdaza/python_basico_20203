import tkinter as tk

def ventana_nueva():
    ventana = tk.Toplevel(root)
    ventana.title("Nueva ventana")
    ventana.geometry("400x400")
    ventana.focus_set()
    boton = tk.Button(ventana, text="Nada")
    boton.pack()

root = tk.Tk()
root.geometry("200x100")
boton = tk.Button(root, text="Nueva", command=ventana_nueva)
boton.pack()
root.mainloop()