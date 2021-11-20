f = open("file.txt", "r")
lines = f.readlines()

f1 = open("file1.txt", "w")
f2 = open("file2.txt", "w")

for line in lines:
    if 'a' in line:
        f1.write(line)
    else:
        f2.write(line)

f1.close()
f2.close()