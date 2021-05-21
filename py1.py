# ****
# ****
# ****
# ****

row = int(input("Enter no. of rows "))
col = int(input("Enter no. of columns "))

def rectangle_1(row, col):
    for dhamaka in range (row):
        for visphot in range (col):
            print("*",end="")
        print()

for dhamaka in range (row):
    print("*"*col)
print()