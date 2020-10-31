import tkinter as tk

def comando():
    print(check_var.get())

ventana = tk.Tk()
check_var = tk.IntVar()
check = tk.Checkbutton(ventana, text="Prueba check", variable=check_var, command=comando)
check.pack()

ventana.mainloop()

