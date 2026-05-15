import tkinter as tk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

fenetre = tk.Tk()
fenetre.title("Cool")
fenetre.geometry("1342x762")
fenetre.configure(bg="black")

image =  tk.PhotoImage(file="image.png")

label = tk.Label(fenetre, image=image)
label.pack()

fenetre.mainloop()
