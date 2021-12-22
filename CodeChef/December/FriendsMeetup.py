t = int(input())
for tc in range(t):
    x1, x2 = map(int, input().split())
    def check(x1, x2):
        if x1 == x2:
            return True
        else:
            diff = x2-x1 if x2>x1 else x1-x2
            x1 += 1
            x2 += 2
            newdiff = x2-x1 if x2>x1 else x1-x2
            if newdiff > diff:
                return False
            check(x1, x2)

    print("NO") if check(x1, x2) == False else print("YES")