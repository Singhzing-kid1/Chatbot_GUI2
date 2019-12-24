from tkinter import *
from tkinter import ttk

def get_sum(event):
    n1 = int(e1.get())
    n2 = int(e2.get())

    s = n1 + n2

    se.delete(0, "end")

    se.insert(0, s)


r = Tk()
r.title("Calculator")

f = Frame(r)

e1 = Entry(f)
l1 = Label(f, text="+")
e2 = Entry(f)

eb = Button(f, text="=")
eb.bind("<Button-1>", get_sum)

se = Entry(f)

e1.pack()
l1.pack()
e2.pack()
eb.pack()
se.pack()

f.pack()



r.mainloop()