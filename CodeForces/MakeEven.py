#by Nikhil Sharma on 26 DEC 2021
#@1:51pm

for _ in range(int(input())):
    n = int(input())
    ans = 0
    if n%2 == 0: ans = '0'
    else:
        n = str(n)
        n = list(map(str, n))
        for i in range(len(n)):
            temp = -1
            if int(n[i])%2 == 0:
                temp = i
                break
        val = 1
        ans = val+1 if temp > 0 else val if temp == 0 else val-2
    print(ans)