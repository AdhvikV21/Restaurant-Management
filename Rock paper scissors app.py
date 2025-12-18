import tkinter as tk
import random

def play(user):
    options = ["Rock", "Paper", "Scissors"]
    comp = random.choice(options)
    if user == comp:
        res = "Tie! Both picked " + comp
    elif (user=="Rock" and comp=="Scissors") or (user=="Paper" and comp=="Rock") or (user=="Scissors" and comp=="Paper"):
        res = "You Won" + user + " beats " + comp
    else:
        res = "You Lost" + comp + "beats" + user
    lbl.config(text=res)

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

tk.Label(root, text="Pick one:").pack()
tk.Button(root, text="Rock", command=lambda: play("Rock")).pack()
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack()
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack()

lbl = tk.Label(root, text="")
lbl.pack()

root.mainloop()