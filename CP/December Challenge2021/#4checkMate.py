#CHECKMATE

import sys, io, os, time
input = sys.stdin.readline

for tc in range(int(input())):
    xk, yk = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    # bring king on the first row (yk = 1)
    if yk == 8:  # turn upside down
        yk, y1, y2 = 9 - yk, 9 - y1, 9 - y2
    elif xk == 1 and yk != 1:  # reflect about main diagonal x = y
        xk, yk, x1, y1, x2, y2 = yk, xk, y1, x1, y2, x2
    elif xk == 8 and yk != 1:
        xk, yk, x1, y1, x2, y2 = yk, xk, y1, x1, y2, x2  # reflect about main diagonal x = y
        yk, y1, y2 = 9 - yk, 9 - y1, 9 - y2  # turn upside down

    if yk != 1:
        print("NO")
        continue

    if xk == 8:  # swap left and right
        xk, x1, x2 = 9 - xk, 9 - x1, 9 - x2

    if xk == 1 and yk == 1 and (x1 == 2 or x2 == 2):
        xk, yk, x1, y1, x2, y2 = yk, xk, y1, x1, y2, x2  # reflect about main diagonal x = y
    if y1 != 2 and y2 != 2:
        print("NO")
        continue
    if (xk - 1 <= x1 and x1 <= xk + 1) or (xk - 1 <= x2 and x2 <= xk + 1) or x1 == x2:
        print("NO")
        continue
    print("YES")