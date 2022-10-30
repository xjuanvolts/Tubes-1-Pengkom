from tkinter import*
from tkinter import ttk

class atm(Tk):
    def __init__(self, root):
        self.root=root
        blank_space=""
        self.root.title(130*blank_space*+"ATM FTI 22")
        self.root.geometry('774x760+280+0')
        self.root(Background='Blue')

start=atm()
start.mainloop()