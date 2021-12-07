"""n = int(input("enter num :"))
for i in range(1, 11):
    print(n*i)
print("Table of : ",n)

while loop

i = int(input("Input any no: "))
while i<11:
    print(i*4)
    i = i+1"""

m = int(input("Enter any Num: "))
for i in range(2,m):
    if m%i == 0:
        print("Not a prime")
        break
else:
    print("its a prime")
