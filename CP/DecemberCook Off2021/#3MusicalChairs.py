#MUSICHAIR

for _ in range(int(input())):
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