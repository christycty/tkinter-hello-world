from tkinter import *

root = Tk()


# display a line when the button is clicked
def my_click():
    my_label = Label(root, text="Button Clicked!")
    my_label.pack()


# state =  DISABLED (cant click) / ACTIVE / NORMAL
# padx, pady = padding (fixed size upon window resize)
# fg:foreground colour, bg: background colour (can use name/hex code)
myButton = Button(root, text="This is a button", command=my_click, fg="blue", bg="aqua")
# use my_click instead of my_click() for command
myButton.pack()

root.mainloop()
