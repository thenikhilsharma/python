#RMNTREV

for _ in range(int(input())):
    size, kk = [*map(int, input().strip().split())]
    st = input().strip()
    vec = ['nope' for i in range(kk)] + list(st[kk: size])
    num = kk
    num -= 1
    check = True
    for i in range(kk):
        # num = k - 1
        if not check:
            vec[num] = st[i]
            num += 2
        if check:
            vec[num] = st[i]
            num -= 2
        if num == -2:
            num = 1
            check = False
        elif num == -1:
            num = 0
            check = False
    ret = ''.join(vec)
    print(ret)