import pickle as pk

f = open("file.dat", "wb")
'''while True:
    str = input("Enter line ")
    f.write(str)
    f.write("\n")
    ch = input("Want to add more line Y/N ")
    if ch == 'N':
        break
print("Lines added to the file ")'''

d1 = {"Name":"Nikhil", "Class":12}
pk.dump(d1, f)