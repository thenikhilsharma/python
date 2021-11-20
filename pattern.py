def lower_triangle(row):

    while (row >= 0):
        print("*"*row)
        row = row - 1
    print()
    # *
    # **
    # ***
    # ****
    # *****
    # ******

def upper_triangle(row):

    for i in range(row,0,-1):
        if row >= 1:
            print("r"*row)
    print()

def crown(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(j, end="")
        print(" "*(2*i), end="")
        for k in range(i+1, n+1):
            print(k, end="")
        print()

crown(5)