#ANTIPAL

for _ in range(int(input())):
    n = int(input())
    ans = 0
    if n%2 != 0: print(-1)
    else:
        hlf = int(n/2)
        print('1'*hlf + '0'*hlf)