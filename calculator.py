from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=50, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Define buttons
# command functions cant intake parameters, but lambda can
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_dot = Button(root, text=".", padx=69, pady=20, command=lambda: button_click("."))

button_plus = Button(root, text="+", padx=29, pady=20, command=button_click)
button_minus = Button(root, text="-", padx=29, pady=20, command=button_click)
button_multiply = Button(root, text="x", padx=30, pady=20, command=button_click)
button_divide = Button(root, text="/", padx=29, pady=20, command=button_click)

button_delete = Button(root, text="DEL", padx=23, pady=20, command=button_click)
button_ac = Button(root, text="AC", padx=23, pady=20, command=button_click)
button_enter = Button(root, text="Enter", padx=55, pady=20, command=button_click)

# Put the buttons on the screen
button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_dot.grid(row=4, column=1,columnspan=2)

button_plus.grid(row=2, column=3)
button_minus.grid(row=2, column=4)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=3, column=4)

button_delete.grid(row=1, column=3)
button_ac.grid(row=1, column=4)
button_enter.grid(row=4, column=3, columnspan=2)


root.mainloop()

"""
simple calculator draft
buttons: 0-9, ., +-*/, clear, enter, del

7   8   9   Del AC
4   5   6   +   -
1   2   3   *   /   
0   .       Enter
"""