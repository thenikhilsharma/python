def appleAndCoupon(n, m, arr):
    marr = arr
    print(marr, arr)
    max_arr = []

    for i in range(m):
        max_arr.append(max(marr))
        marr.pop(marr.index(max(marr)))
    print(arr, marr, max_arr)

    free_apple = []
    for i in range(m):
        free_apple.append(arr.index(max_arr[i]))
    free_apple = arr[max(free_apple)]

n, m = map(int, input().split())
array = list(map(int, input().split()))
appleAndCoupon(n, m, array)