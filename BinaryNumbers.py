import stack

n = int(input())

binary = bin(n).replace("0b", "")

l = list(binary)
print(l)
b = 1
blist = []

for i in range(len(l)):
    print(l[i])
    if l[i] == 1:
        b = b+1
        blist.append(b)
    elif l[i] == 0:
        b = 1
print(blist)