tc = int(input())
for t in range(tc):
    i = input()
    p = input()
    i = list(map(str, i))
    p = list(map(str, p))
    #print(i, p)
    ans, index, n = 0, 0, 0
    if len(p) < len(i):
        ans = 0
    else:
        #print(len(p), len(i))
        for x in range(len(i)):
            if p[x] == i[x]:
                print(p[x], i[x])
                continue
            else:
                print(p[x], i[x])
                del p[x]
                ans += 1
            #index += 1
            n = len(p) - len(i)
            print(n)
        ans+=n
    
    print("Case #%d: %d" %(t+1, ans))