#SOlved

for tc in range(int(input())):
    n = int(input())
    n -= 1
    i, ans = 1, 0
    while(i*i<=n):
        if(n%i==0):
            ans += 1
            if(i*i != n):
                ans += 1
        i += 1
    print(ans)

'''
for tc in range(int(input())):
    n = int(input())
    half = int((n-1) / 2)
    if n > 2:
        ways = 1
        for i in range(1,half+1):
            if (n-1)%i == 0:
                print(n-1, i)
                ways += 1
            else: continue
        print(ways)
    elif n == 1 or n == 2: print(1)
    else: print(0)'''