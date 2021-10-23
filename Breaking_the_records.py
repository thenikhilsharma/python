n = int(input())

arr = list(map(int, input().split()))

max = int(arr[0])
min = int(arr[0])
x = 0
n = 0

for i in range(1, len(arr)):

    if int(arr[i]) > max:
        max = int(arr[i])
        x = x+1

    elif arr[i] < min:
        min = int(arr[i])
        n = n+1

print(x, n)