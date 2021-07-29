def check_Variable(input):
    if input=="A":
        print("010000011")
    elif input=="B":
        print("01000010")
    elif input=="C":
        print("01000011")
    elif input=="D":
        print("01000100")
    elif input=="E":
        print("01000101")
    elif input=="F":
        print("01000110")
    elif input=="G":
        print("01000110")
    elif input=="H":
        print("01000110")
    elif input=="I":
        print("01001001")
    elif input=="J":
        print("01001010")
    elif input=="K":
        print("01001011")
    elif input=="L":
        print("01001100")
    elif input=="M":
        print("01001101")
    elif input=="N":
        print("01001110")
    elif input=="O":
        print("01001111")
    elif input=="P":
        print("01010000")
    elif input=="Q":
        print("01010001")
    elif input=="R":
        print("01010010")
    elif input=="S":
        print("01010011")
    elif input=="T":
        print("01010100")
    elif input=="U":
        print("01010101")
    elif input=="V":
        print("01010110")
    elif input=="W":
        print("01010111")
    elif input=="X":
        print("01011000")
    elif input=="Y":
        print("01011001")
    elif input=="Z":
        print("01011010")

enter = input("Enter ur variable")
for i in range(len(enter)):
    value = enter[i]
    check_Variable(value)