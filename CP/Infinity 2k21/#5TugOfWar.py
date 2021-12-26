#by Nikhil Sharma on 23 dec
#TOW

for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    save = []
    for i in b:
        save.append(i)

    def checkSame(x, y):
        return (True if x == y else False)

    def order(a, b):
        b.sort()
        ansarray = []
        for i in a:
            for j in b:
                if i == j or i <= j:
                    ansarray.append(j)
                    del b[b.index(j)]
                    break 
        ansarray += b
        return ansarray
    

    ans = order(a, b)
    if checkSame(save, ans) == False:
        print("YES")
        for i in ans:
            print(i, end=' ')
        print('')
    else: print("NO")