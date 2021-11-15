n = int(input())
arr = list(map(int, input().split()))

arrMax = max(arr)
arr.sort()
print(arr)

for i in range(-len(arr),-1):
    if arr[i] != arrMax:
        print(i)
        print(arr[i])
        break