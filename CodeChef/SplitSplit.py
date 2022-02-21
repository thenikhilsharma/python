#By Nikhil Sharma on 20 dec 2021
#@ 1:42 am

for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 'NO'
    half = int((n+1)/2) if n%2 != 0 else int(n/2)
    for i in range(n-1, -1, -1):
        a, b = s[:i], s[i:]
        if b in a:
            ans = 'YES'
            break
        if i == half:
            break

    print(ans)