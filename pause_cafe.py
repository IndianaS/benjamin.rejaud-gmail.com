import time
import tkinter
from tkinter import *

import pyautogui


class Pause_cafe:

    def deplace_souris(self):
        while True:
            time.sleep(600)
            pyautogui.move(150, 150, 3, pyautogui.easeInElastic)
            pyautogui.move(-150, -150, 3, pyautogui.easeInElastic)
"""
def action():
    run = Pause_cafe()
    run.deplace_souris()

# fenetre de l'appli
windows = Tk()
windows.title("Pause café")
windows.geometry("500x60")
windows.minsize(500, 60)

#Ajout logo
windows.iconbitmap("Picture/Pause_café.ico")

#Titre appli
Label_title = Label(windows, text="Bienvenue sur l'application Pause café", font=("Verdana"))
Label_title.pack()

# Widgets
button_break = tkinter.Button(windows, text="Lancer la pause", width=20, command=action)

button_break.pack()
# Afficher fenetre
windows.mainloop()
"""