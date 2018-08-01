from random import randint
import tkinter as tk

# reestructure project to have each object in a file, and use main file for logic

root= tk.Tk()
root.title('dice roller')

labeltitle = tk.Label(root, text="roll dice again? ")
labeltitle.pack()

buttonYes= tk.Button(root, text="Yes", fg="blue")
buttonYes.pack()
buttonNo= tk.Button(root, text="No", fg="red")
buttonNo.pack()

label1 = tk.Label(root, text='first dice:' + str(dice1))
label1.pack()

root.mainloop()
