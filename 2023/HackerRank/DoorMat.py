for _ in range(int(input())):
    N, M = map(int, input().split())
    #print(N, M)
    y = M//2
    x = y - 1
    z = 1

    for i in range(N//2):
        print('-'*x, '.|.'*z, '-'*x, sep='')
        x -= 3
        z += 2
    print('-'*(y-3), 'WELCOME', '-'*(y-3), sep='')
    for i in range(N//2):
        x = x+3
        z -= 2
        print('-'*x, '.|.'*z, '-'*x, sep='')
