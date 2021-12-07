#by Nikhil Sharma on 1Dec
#@8:41 solved

t = int(input())
for j in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    kthPlace = s[k-1]
    count = 0

    for i in s:
        if i >= kthPlace:
            count += 1

    print(count)