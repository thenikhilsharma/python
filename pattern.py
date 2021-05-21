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

upper_triangle(6)