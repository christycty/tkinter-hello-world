from tkinter import *

#create window
root = Tk()

#create mylabel widget
myLabel = Label(root, text="Hello World")
#showing it onto the screen
myLabel.pack()

#else it will immediately disappear
root.mainloop()
