#MXMTRIO

for ct in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a3 = max(a)
    a2 = min(a)
    del a[a.index(max(a))]
    a1 = max(a)

    SUM = (a3-a2)*a1
    print(SUM)