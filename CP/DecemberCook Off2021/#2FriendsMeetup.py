#FRIMEET

for _ in range(int(input())):
    x1, x2 = map(int, input().split())
    if x1 == x2: print("YES")
    elif x1 < x2: print("NO")
    elif x1 > x2: print("YES")