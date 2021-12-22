file = open('file.txt','r+')

#file.write("This is the write command, w mode\n")
#file.write("it allows us to write in a parcticular file, w mode\n")
#file.write("This will append this line, a mode\n")
print(file.read())
print(file.tell())    #current pos of curser
file.seek(0)          #gets cursor to initial pos

file.close()