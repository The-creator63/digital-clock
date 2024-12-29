#importing liabraries
from tkinter import*
from tkinter.ttk import*
from time import strftime #function to retreive systems time

#creating GUI
root = Tk()
root.title("Clock")

lbl = Label(root,font = ("Times",40,"bold"),background = "black",foreground = "white")
lbl.pack(anchor = "center")

#creating the function
def time():
    clock = strftime("%H:%M:%S %p")
    lbl.config(text = clock)
    lbl.after(1000,time)

time()
root.mainloop()