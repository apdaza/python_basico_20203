import tkinter as tk

def responder():
    print("Excelente")

root = tk.Tk()
boton = tk.Button(root, text="Que te parece el ejemplo?", command=responder)
boton.pack()
root.mainloop()