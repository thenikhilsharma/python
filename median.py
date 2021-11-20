n = int(input())
L = list(map(int, input().split()))

for i in range (n):
    k = L[i]
    j = i-1
    while j>=0 and k<L[j]:
        L[j+1] = L[j]
        j = j-1
    else:
        L[j+1] = k

if n//2 != 0:
    z = int(n / 2)
    print(L[z])