from tkinter import *
# create gui window
window = Tk()


def from_kg():
    # convert kg to gram
    gram = float(e2_value.get()) * 1000

    # convert kg to pound
    pound = float(e2_value.get()) * 22.0462

    # convert kg to ounce
    ounce = float(e2_value.get()) * 35.274

    # Enters the conveted weight to the text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t1.delete("1.0", END)
    t1.insert(END, pound)

    t1.delete("1.0", END)
    t1.insert(END, ounce)


# create the Label widgets
e1 = Label(window, text="Enter the weight in Kg")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='Gram')
e4 = Label(window, text='Pounds')
e5 = Label(window, text='Ounce')

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

b1 = Button(window, text="Convert")

# grid method is used for placing
# the widget at respective positions
# in the table like structure

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=3)

# start the gui
window.mainloop()