from tkinter import *
import os
import tkinter.messagebox

root = Tk()

a = Entry(root,bg="black",fg="lawn green",width=30)
a.insert(0,"enter the password: ")
a.grid(row=2,column=2)

def enter():
    path ="C:\\ace\\ace.py"
    os.startfile(path)


def comment():
    password = "vishu"
    if(a.get()==password):
       enter()
    else:
        tkinter.messagebox.showinfo("error","try again..")

button = Button(root,text="submit",command=comment,fg="lawn green",bg="black")
button.grid(row=5,column=2)

root.geometry("200x200")
root.mainloop()