from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox,font
from tkinter import ttk
from datetime import datetime
import webbrowser

def new():
    text.delete('1.0','end')

def newWindow():
    root = tk.TK()
    root.geometry('500x500')

    menubar = Menu(root)

    file = Menu(menubar,tearoff = 0)
    file.add_command(label="New Chat",command=new)
    file.add_command(label="New Chat Room",command=new_window)
    file.add_command(label="Open another Room",command=new)
    file.add_command(label="Save chat",command=new)
    file.add_command(label="Save chat as",command=new)
    file.add_separator()
    file.add_command(label="End chat",command=new)
    menubar.add_cascade(label="Chat",menu=file,font="verdana",10,"bold")