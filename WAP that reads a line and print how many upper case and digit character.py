line = input()
u = 0
d = 0
for a in line:
    if a.isupper():
        u = u+1
    if a.isdigit():
        d = d+1
print(u,d)
