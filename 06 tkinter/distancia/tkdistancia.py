from tkinter import *
from punto import Punto

class TkDistancia:

    def __init__(self):
        self.root = Tk()
        self.p1 = Punto(0, 0)
        self.p2 = Punto(0, 0)
        self.frame = Frame(self.root)
        self.frame.pack()

        self.lbl_punto1 = Label(self.frame, text="Punto 1: ", font=("Helvetica", 30))
        self.lbl_punto1.pack()

        self.coordenadas1 = StringVar()
        self.txt_punto1 = Entry(self.frame, textvariable=self.coordenadas1)
        self.txt_punto1.pack()

        self.lbl_punto2 = Label(self.frame, text="Punto 2: ", font=("Helvetica", 30))
        self.lbl_punto2.pack()

        self.coordenadas2 = StringVar()
        self.txt_punto2 = Entry(self.frame, textvariable=self.coordenadas2)
        self.txt_punto2.pack()

        self.distancia = StringVar()
        self.lbl_distancia = Label(self.frame, textvariable=self.distancia, font=("Helvetica", 30))
        self.lbl_distancia.pack()

        self.boton_iniciar = Button(self.frame, text="Calcular", command=self.calcular)
        self.boton_iniciar.pack()

        self.root.mainloop()

    def calcular(self):
        punto1 = [int(x) for x in self.coordenadas1.get().split(",")]
        punto2 = [int(x) for x in self.coordenadas2.get().split(",")]

        self.p1.x = punto1[0]
        self.p1.y = punto1[1]

        self.p2.x = punto2[0]
        self.p2.y = punto2[1]

        distancia = self.p1.calcular_distancia(self.p2)

        self.distancia.set(str(distancia))

app = TkDistancia()
