#TWOROOKS
#got to know the approach later by my own

for _ in range(int(input())):
    x1,y1,x2,y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        print("YES")
    else: print("NO")