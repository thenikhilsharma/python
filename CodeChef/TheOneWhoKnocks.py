#unsolved

for tc in range(int(input())):
    x, y = map(int, input().split())

    diff = y - x
    if diff > 0 and diff % 2 != 0:
        print(1)
    else:
        print(2)