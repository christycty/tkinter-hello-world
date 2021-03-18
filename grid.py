from tkinter import *


root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Nice to meet you!")
myLabel3 = Label(root, text="      ")

# wont resize with window size
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=0, column=1)
# r/c not fixed size, they are just relative (order of widgets)

"""
#lazier representation
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text="Nice to meet you!").grid(row=1, column=2)
myLabel3 = Label(root, text="      ").grid(row=0, column=1)
"""
root.mainloop()
