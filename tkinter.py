from tkinter import *
from tkinter.ttk import *

top = Tk()
top.title("Calc")
top.geometry('350x500')

user_name = Label(top, text = "Username").place(x = 40,y = 60)
user_password = Label(top, text = "Password").place(x = 40,y = 100) 
submit_button = Button(top, text = "Submit").place(x = 40,y = 130)
user_name_input_area = Entry(top,width = 30).place(x = 110,y = 60)    
user_password_entry_area = Entry(top,width = 30).place(x = 110,y = 100)

button = Button(top, text="Start", command=top.destroy)
button.pack(side ='top')

v = StringVar(top, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1","RadioButton 2" : "2","RadioButton 3" : "3","RadioButton 4" : "4","RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(top, text = text, variable = v,value = value).pack(side=BOTTOM, ipady = 5)

mainloop()
