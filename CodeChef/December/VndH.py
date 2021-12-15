t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    ans = ""

    if m == n:
        for i in range (0, n, 1):
            ans += "01"
    
    elif m > n:
        for i in range(0, n, 1):
            ans += "10"

        for i in range(0, m-n, 1):
            ans += "110"

        ans += "1"
    else:
        for i in range(0, m, 1):
            ans += "01"
            
        for i in range(0, n-m, 1):
            ans += "010";
        
    print(len(ans))
    print(ans)