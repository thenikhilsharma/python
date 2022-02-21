for tc in range(int(input())):
    n, b = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    total = 0
    count = 0

    for element in a:
        total += element
        if total <= b: count += 1
        else: break
    
    print('Case #%d: %d' % (tc+1, count))