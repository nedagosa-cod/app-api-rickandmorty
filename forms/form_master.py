import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
import requests
from PIL import ImageTk, Image
import io
import json


class MasterPanel:

        def __init__(self):
            self.ventana = tk.Tk()
            self.ventana.title("Master Panel")
            w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
            self.ventana.geometry("%dx%d+0+0" % (w, h))
            self.ventana.config(bg='#fcfcfc')
            self.ventana.resizable(width=0, height=0)

            logo = utl.leer_imagen("./img/logo.png", (200,200))

            # CONTAINER IZQUIERDA LOGO
            frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10,bg='#00416a')
            frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
            label = tk.Label( frame_logo, image=logo, bg='#00416a')
            label.place(x=0,y=0, relwidth=1, relheight=1)

            # CONTAINER DERECHA DE CARDS
            frame_right = tk.Frame(self.ventana, bg='#baddff')
            frame_right.pack()


            response = requests.get("https://rickandmortyapi.com/api/character")
            personajes = response.json()["results"]

            numMaxColums = 6
            numMaxCards = 20
            contador = 0
            arrImagenes = []

            for i in range(numMaxColums):
                for j in range(numMaxCards // numMaxColums):
                    frame_card = tk.Frame(frame_right, width=150, height=220, bd=2, relief=tk.SOLID, bg='#00416a')
                    frame_card.grid(row=j, column=i, padx=5, pady=5)

                    personaje = personajes[contador]

                    img = utl.leer_imagen_web(personaje['image'],(100,130))
                    arrImagenes.append(img)

                    label_img = tk.Label(frame_card, image=img, bg='#00416a', width=150)    
                    label_img.grid(row=1, column=1)

                    label_text = tk.Label(frame_card, text=personaje['name'], font=('Times',12), fg="#ffffff", bg='#00416a', pady=4, width=15)
                    label_text.grid(row=2, column=1)

                    label_especie = tk.Label(frame_card, text=personaje['species'], font=('Times',10), fg="#ffffff", bg='#00416a', pady=4, width=15)
                    label_especie.grid(row=3, column=1)

                    label_especie = tk.Label(frame_card, text=personaje['status'], font=('Times',10), fg="#ffffff", bg='#00416a', pady=4, width=15)
                    label_especie.grid(row=4, column=1)

                    contador = contador + 1

            self.ventana.mainloop()