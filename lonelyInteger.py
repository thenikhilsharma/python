c = int(input())

a = list(map(int, input().split()))
notCom = []
b = []

for i in range (c):
    for j in range(c):
        b = a[0:c] - a[i]
        if a[i] == a[j]:
            COM = COM+1
        else:
            notCom.append(a[i])

print(notCom)