s, t = input().split()
s = int(s)
t = int(t)
house = []
appCount = 0
oraCount = 0

for i in range(s,t+1):
    house.append(i)
length = len(house)

a, b = input().split()
m, n = input().split()
a = int(a)
b = int(b)
m = int(m)
n = int(n)

apples = list(input().split())
oranges = list(input().split())

for Acount in apples:
    Sum = int(Acount) + a
    for j in range(length):
        if Sum == int(house[j]):
            appCount = appCount+1
            break

for Ocount in oranges:
    OSum = int(Ocount) + b
    for k in range(length):
        if OSum == int(house[k]):
            oraCount = oraCount+1
            break

print(appCount)
print(oraCount)