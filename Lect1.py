a = int(input("NUM 1 : "))
b = int(input("NUM 2 : "))

print("For sum press 1")
print("For subtract press 2")
print("For divide press 3")
print("For multiply press 4")
print("For remainder press 5")
print("For exponent press 6")

inp = int(input("I said what i want to say, Now you say : "))

if inp == 1:
 print("you Asked for ADDITION, here it is : ", a+b)
elif inp == 2:
 print("you Asked for SUBTRACTION, here it is : ", a-b)
elif inp == 3:
 print("you Asked for DIVISION, here it is : ", a/b)
elif inp == 4:
 print("you Asked for MULTIPLICATION, here it is : ", a*b)
elif inp == 5:
 print("you Asked for REMAINDER, here it is : ", a//b)
elif inp == 6:
 print("you Asked for EXPONENT, here it is : ", a**b)
