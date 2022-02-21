for _ in range(int(input())):
    l1, l2, l3 = map(int, input().strip().split())
    mx = max([l1,l2,l3])

    if mx == l1:
        if l2+l3 == mx: print('YES')
        elif l2 == l3 and mx%2 == 0: print('YES')
        elif l1 == l2 and l3%2 == 0: print('YES')
        elif l1 == l3 and l2%2 == 0: print('YES')
        else: print('NO')
    elif mx == l2:
        if l1+l3 == mx: print('YES')
        elif l1 == l3 and mx%2 == 0: print('YES')
        elif l2 == l1 and l3%2 == 0: print('YES')
        elif l2 == l3 and l1%2 == 0: print('YES')
        else: print('NO')
    elif mx == l3:
        if l2+l1 == mx: print('YES')
        elif l2 == l1 and mx%2 == 0: print('YES')
        elif l1 == l3 and l1%2 == 0: print('YES')
        elif l3 == l2 and l2%2 == 0: print('YES')
        else: print('NO')