n = int(input())
arr = list(map(int, input().split()))

arrMax = max(arr)
arr.sort()
print(arr)

for i in range(-1,-len(arr)):
    if arr[i] != arrMax:
        print(i)
        print(arr[i])
        break