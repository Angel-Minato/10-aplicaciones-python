from tkinter import *  
from tkinter import messagebox
from backend import Database

db = Database("libro.db")

def seleccionado(event):
    try:
        global selec
        index=list1.curselection()[0]
        selec=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selec[1])
        e2.delete(0,END)
        e2.insert(END,selec[2])
        e3.delete(0,END)
        e3.insert(END,selec[3])
        e4.delete(0,END)
        e4.insert(END,selec[4])
        print (selec)
    except IndexError:
        pass    

def ver_comando():
    list1.delete(0,END)
    for row in db.view():
        list1.insert(END,row)

def buscar_comando():
     list1.delete(0,END)
     for row in db.busqueda(titulo_txt.get(),autor_txt.get(),year_txt.get(),ISBN_txt.get() ):
         list1.insert(END,row)

def agregar():
    db.insert(titulo_txt.get(),autor_txt.get(),year_txt.get(),ISBN_txt.get())
    list1.delete(0,END)
    list1.insert(END,titulo_txt.get(),autor_txt.get(),year_txt.get(),ISBN_txt.get())

def eliminar_comando():
    confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este registro?")
    if confirmacion:
        db.delete(selec[0])
        messagebox.showinfo("Accion completada", "Eliminación completada")
        ver_comando()  # Para actualizar la lista después de eliminar
    else:
        messagebox.showinfo("Accion completada", "Eliminación cancelada")
        print("Eliminación cancelada")

def actualizar_comando():
    db.update(selec[0],titulo_txt.get(),autor_txt.get(),year_txt.get(),ISBN_txt.get())
    print(selec[0],titulo_txt.get(),autor_txt.get(),year_txt.get(),ISBN_txt.get())    

window = Tk()

window.wm_title("Libros")

l1 = Label(window,text="Titulo")
l1.grid(row=0,column=0)

l2 = Label(window,text="Autor")
l2.grid(row=0,column=2)

l3 = Label(window,text="Año")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

titulo_txt=StringVar()
e1=Entry(window,textvariable=titulo_txt)
e1.grid(row=0,column=1)

autor_txt=StringVar()
e2=Entry(window,textvariable=autor_txt)
e2.grid(row=0,column=3)

year_txt=StringVar()
e3=Entry(window,textvariable=year_txt)
e3.grid(row=1,column=1)

ISBN_txt=StringVar()
e4=Entry(window,textvariable=ISBN_txt)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',seleccionado)

b1=Button(window,text="ver todo" ,width=12,command=ver_comando)
b1.grid(row=2,column=3)

b2=Button(window,text="Buscar" ,width=12,command=buscar_comando)
b2.grid(row=3,column=3)

b3=Button(window,text="Agregar" ,width=12,command=agregar)
b3.grid(row=4,column=3)

b4=Button(window,text="Actualizar" ,width=12,command=actualizar_comando)
b4.grid(row=5,column=3)

b5=Button(window,text="Eliminar" ,width=12,command=eliminar_comando)
b5.grid(row=6,column=3)

b6=Button(window,text="Cerrar" ,width=12, command=window.destroy)
b6.grid(row=7,column=3)



window.mainloop()