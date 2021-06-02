#importing 
from tkinter import *
import tkinter as tk
import tkinter.font as TkFont

root = tk.Tk()

root.title("HeLLo")
root.iconbitmap(r'D:\Downloads\study.ico')
root['bg'] = "cyan"

font1 = TkFont.Font(family="Helvetica",size=12,weight="bold")

root.geometry("350x450")
root.maxsize(500,700)
root.minsize(200,200)

l1 = Label(root, text = "Email", font=font1, bg="cyan",fg="red")
l2 = Label(root, text = "Password", font=font1, bg="cyan", fg="red")

l1.grid(row = 1,column = 1,pady = 10,padx = 15)
l2.grid(row = 2,column = 1,pady = 4,padx = 15)

emailField = Entry(root)
passField = Entry(root)

emailField.grid(row=1, column=2,pady=10)
passField.grid(row=2,column=2,pady=4)

keepSigned = Checkbutton(root, text="Keep me signed in", bg="cyan",fg="red")
keepSigned.grid(row=3, column="2", padx=60,pady=10)

submiteBTN = Button(root,text="LOGIN")
submiteBTN.grid(column=2,row=4,pady="3")

root.mainloop()

"""userName = input(" Hello Dear User\nThanks for using this app\n Please enter your name :")
print("Hi, ",userName)"""