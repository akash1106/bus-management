from tkinter import *
from tkinter import ttk

win=Tk()

w1=LabelFrame(win)

mycanvas=Canvas(w1)
mycanvas.pack(side=LEFT)

yscroll=ttk.Scrollbar(w1,orient="vertical",command=mycanvas.yview)
yscroll.pack(side=RIGHT,fill="y")

mycanvas.configure(yscrollcommand=yscroll.set)

mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe=Frame(mycanvas)
mycanvas.create_window((0,0),window=myframe,anchor="nw")
w1.pack(fill="both")

for i in range(100):
    Button(myframe,text=str(i)).pack()

win.geometry("500x500")
win.mainloop()