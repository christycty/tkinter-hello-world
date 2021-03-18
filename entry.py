from tkinter import *

root = Tk()

# input box
e = Entry(root, width=50, fg="blue", bg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name")  # default text


# e.get: return string in entry box, wont clear entry box
def my_click():
    hello = "Hello " + e.get()  # display string
    my_label = Label(root, text=hello)
    my_label.pack()


myButton = Button(root, text="Enter", command=my_click)
myButton.pack()

root.mainloop()