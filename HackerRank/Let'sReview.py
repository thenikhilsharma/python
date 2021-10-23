n = int(input("Enter no of test cases"))
s = input()

l1 = []
l2 = []

for i in range (0, len(s), 2):
    l1.append(s[i])
for j in range (1, len(s), 2):
    l2.append(s[j])

print(l1, l2)