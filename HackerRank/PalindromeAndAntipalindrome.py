setInp = []
finalList = []

noCases = int(input("Enter no. of elements"))

for i in range(noCases):
    print(i)
    value = int(input("Enter Value for "))
    setInp.append(value)

length = len(setInp)

def check():
    l = 0
    while l<length:
        if setInp[l] != 1 or 0:
            print("Value out of index")
        else:
            print("Correct input")

        l = l+1

check()

print(setInp)

finalList = setInp.reverse()

print(finalList)

if finalList == setInp:
    print("Palindrome")
else:
    print("get lost")
