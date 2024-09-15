import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 50), background="black", foreground="cyan")
label.pack(anchor='center')

time()
root.mainloop()
