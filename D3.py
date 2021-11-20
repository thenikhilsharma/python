n = int(input())
arr = list(map(int, input().split()))

for i in range (n):
    k = arr[i]
    j = i-1
    while j>=0 and k<arr[j]:
        arr[j+1] = arr[j]
        j = j-1
    else:
        arr[j+1] = k
        print(arr)

max = max(arr)

arr