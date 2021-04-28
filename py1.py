value = int(input("Enter row value "))
value2 = int(input("Enter Column value "))

for row in range(value):
    for col in range(value2):
        print("*",end="")
    print()