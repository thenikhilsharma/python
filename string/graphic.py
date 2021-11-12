from tkinter import *

screen = Tk()
screen.title("Program")

screen.geometry("500x500")

welcome_text = Label(text = "welcome", fg = "red", bg = "yellow")
welcome_text.pack()

click_me = Button(text = "Click Me", fg = "red", bg = "yellow")
click_me.place(x = 10, y = 20)
