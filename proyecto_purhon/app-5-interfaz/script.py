from tkinter import *

window=Tk()

def escriba():
    conv = float(el_sapito.get())*1.9
    txt.insert(END,conv)

b1=Button(window, text="Boton",command=escriba)
b1.grid(row=0, column=0)

el_sapito = StringVar()
e1= Entry(window,textvariable=el_sapito)
e1.grid(row=0, column=1)

txt = Text(window,height=1,width=20)
txt.grid(row=0, column=2)

window.mainloop()