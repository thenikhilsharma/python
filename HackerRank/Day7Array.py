n = int(input())

l = list(map(int, input().split()))

m = []

for i in range(n-1, -1,-1):
    m.append(l[i])
    print(l[i], end=" ")