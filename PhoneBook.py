n = int(input())
L = []

for i in range(n):
    l = list(input().split())
    L.append(l)
    
a = len(L)

for j in range(n):
    b = input()
    c = 0
    for k in range(a):
        if b == L[k][0]:
            print(L[k][0],"=",L[k][1], sep="")
            pass
        else:
            c = c+1
        if c == n:
            print("Not found")