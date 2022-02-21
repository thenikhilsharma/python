def operation(arr, n, k, ans):
    if k == 0:
        for i in range(n):
            print(arr[i], end = ' ')
        print('')
    else:
        [ans.append(arr[i]) for i in range(0, n, 2)]
        [ans.append(arr[i]) for i in range(1, n, 2)]
        return operation(ans, n, k-1, [])

for _ in range(int(input())):
    n, k = map(int, input().split())    #input num, no of operations
    operation(range(1, n+1), n, k, [])

for _ in range(int(input())):
    n, k = map(int, input().split())
    n -= 1
    for i in range(n+1):
        if (2<<i) % n == 1:
            ct = i+1
            break
    itr = n+1 if ct==k else (1<<k)%n if ct>k else 1<<(k%ct)%n

    z = 0
    for i in range(n+1):
        print(z+1, end=' ')
        z = (z+itr)%n
        if z == 0: z = n
    print()