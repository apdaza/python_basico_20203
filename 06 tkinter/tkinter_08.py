import tkinter as tk

def operacion():
    print("la opcion es: " + variable.get())

root = tk.Tk()
variable = tk.StringVar()
radio1 = tk.Radiobutton(root, text="1", variable=variable, value=1, command=operacion)
radio2 = tk.Radiobutton(root, text="2", variable=variable, value=2, command=operacion)
radio1.pack()
radio2.pack()
root.mainloop()