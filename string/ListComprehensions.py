#by Nikhil Sharma on 15 Nov 2021
#HackerRank
#time complexity ki lagi padi h

x = int(input())
y = int(input())
z = int(input())
n = int(input())

parry, qarry, rarry = [], [], []
for p in range(x+1):
    parry.append(p)
for q in range(y+1):
    qarry.append(q)
for r in range(z+1):
    rarry.append(r)

arr = []
for a in parry:
    for b in qarry:
        for c in rarry:
            lst = [a,b,c]
            arr.append(lst)

for m in range(len(arr)):
    if sum(arr[m]) == n:
        print(arr[m])#by Nikhil Sharma on 15 Nov 2021
#HackerRank

x = int(input())
y = int(input())
z = int(input())
n = int(input())

parry, qarry, rarry = [], [], []
for p in range(x+1):
    parry.append(p)
for q in range(y+1):
    qarry.append(q)
for r in range(z+1):
    rarry.append(r)

arr = []
for a in parry:
    for b in qarry:
        for c in rarry:
            lst = [a,b,c]
            arr.append(lst)

sarry = []
for m in range(len(arr)):
    if sum(arr[m]) < n or sum(arr[m]) > n:
        sarry.append(arr[m])
print(sarry)