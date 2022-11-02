from tkinter import *

tubes= Tk()
tubes.config(background="red")

label=Label(text='Tubes Pengkom', font="Arial 30",background="white")

label.grid(row=10,column=10)

button=Button(text="Tekan",font='Normal 10')
button.grid(row=1,column=1)

tubes.mainloop()