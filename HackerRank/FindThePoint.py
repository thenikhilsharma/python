T = int(input())

def FindPoint(arr):
    px = arr[0]
    py = arr[1]
    qx = arr[2]*2
    qy = arr[3]*2

    rx = qx - px
    ry = qy - py

    print(rx, ry)

for i in range (T):
    arr = list(map(int, input().split()))
    FindPoint(arr)
