from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x150")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('Arial', 40, 'bold'),
              background='black',
              foreground='white')
label.pack(anchor='center')

time()
root.mainloop()